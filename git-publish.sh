echo 
echo ----------------------------------------------------------------------------
echo Automatically add all files, commit and publish to remote repository
echo ----------------------------------------------------------------------------

# Check if there is any unstaged
dirtyFiles=`git status --porcelain 2>/dev/null| egrep "^??" | wc -l`

if [ $dirtyFiles == 0 ] ; then
    echo "Nothing to commit"
    read -p "Press any key to continue... " -n1 -s
    exit 1
fi

# Path of the version file
versionFile="${PWD}/VERSION"

# Read the first line to determine current version
currentVersion=$(head -n 1 $versionFile)

# Establish variables
version=$(echo $currentVersion | cut -f1 -d ' '  )
buildNumber=$(echo $currentVersion | cut -f3 -d ' ' )

# Push message
pushMessage=$(echo Auto publish $currentVersion)


# Check if the version is already in the repository
tags=`git tag` # Get all tags as space separated strings

doAddTag=1

for tag in $tags
do
        if [ "$version" == "$tag" ] ; then
            # Disable add tag if found
            doAddTag=0
        fi
done



# Perform commit and push
echo 
echo "Uploading Changes to GitHub"
echo -----------------------------
echo 

git add --all
git commit -m "\"$pushMessage\""
git push origin master

# Add tag if not found
if [ $doAddTag == 1 ] ; then
    echo 
    echo "Version incremented, adding new tag"
    echo -------------------------------------
    echo 
    git tag -a "$version" -m "Version $version"
    git push --tags
fi

read -p "Press any key to continue... " -n1 -s