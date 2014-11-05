import armacode
import rhinoscriptsyntax as rs
brep_id = rs.GetObject("Polysurface", rs.filter.polysurface, preselect=True)

rc = rs.EnableRedraw(False)
#Unfold as a Cross

#rc = armacode.UnfoldBrep(brep_id, 4, 0)
#print rc
#rc = armacode.UnfoldBrep(brep_id, 4, 3)
#print rc
#rc = armacode.UnfoldBrep(brep_id, 4, 2)
#print rc
#rc = armacode.UnfoldBrep(brep_id, 4, 1)
#print rc

#Unfold as a T shape

#rc = armacode.UnfoldBrep(brep_id, 4, 0, 2, 3)
#print rc
#rc = armacode.UnfoldBrep(brep_id, 4, 1)
#print rc
#rc = armacode.UnfoldBrep(brep_id, 0, 2)
#print rc
#rc = armacode.UnfoldBrep(brep_id, 0, 3)
#print rc

rc = armacode.UnfoldBrep(brep_id, 4, 1)
print rc
rc = armacode.UnfoldBrep(brep_id, 4, 0)
print rc
rc = armacode.UnfoldBrep(brep_id, 4, 2)
print rc
rc = armacode.UnfoldBrep(brep_id, 4, 3, 5)
print rc
rc = armacode.UnfoldBrep(brep_id, 3, 5)
print rc

print rc
rc = rs.EnableRedraw(True)
print rc
