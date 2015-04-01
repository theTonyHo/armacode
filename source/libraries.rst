.. A few words
Libraries
=========

    Library of all the useful methods which can be used during the development of a script or a workflow sequence. 

Each of the method should Only perform one small single purpose. For example::

    Add(x,y):
        result = x + y
        return result
    
    Average(x,y):
        result = Add(x,y) / 2 
        return result

.. Note:: Average function reuses Add function to reduce data redundancy and help code management.

Access the method with the following::

    import armacode
    line = armacode.AddLine()


.. contents::
   :maxdepth: 2
   :local:
   

.. include:: armacode/libraries/AddBlock.rst
.. include:: armacode/libraries/AddDimAlignedFromLine.rst
.. include:: armacode/libraries/AddDimLinearFromLine.rst
.. include:: armacode/libraries/AddLayer.rst
.. include:: armacode/libraries/AddLineEX.rst
.. include:: armacode/libraries/AddLinearDimension.rst
.. include:: armacode/libraries/AddObjectsToBlock.rst
.. include:: armacode/libraries/AddPlaneSurfaceCenter.rst
.. include:: armacode/libraries/AnnotationProperties.rst
.. include:: armacode/libraries/AnnotationText.rst
.. include:: armacode/libraries/BlockInstanceBasePlane.rst
.. include:: armacode/libraries/BlockModify.rst
.. include:: armacode/libraries/BlockProperties.rst
.. include:: armacode/libraries/BrepEdgeCreaseAngle.rst
.. include:: armacode/libraries/BrepEdges.rst
.. include:: armacode/libraries/BrepReorderFaces.rst
.. include:: armacode/libraries/BrepSplitWithCurves.rst
.. include:: armacode/libraries/CSVOpen.rst
.. include:: armacode/libraries/CSVRead.rst
.. include:: armacode/libraries/CSVWrite.rst
.. include:: armacode/libraries/ClearUserText.rst
.. include:: armacode/libraries/CommonEdge.rst
.. include:: armacode/libraries/CreaseAngle.rst
.. include:: armacode/libraries/CurveDuplicates.rst
.. include:: armacode/libraries/CurveSplitOverlap.rst
.. include:: armacode/libraries/DebugArray2D.rst
.. include:: armacode/libraries/DebugCurveDeviation.rst
.. include:: armacode/libraries/DebugLine.rst
.. include:: armacode/libraries/DebugValues.rst
.. include:: armacode/libraries/DebugVector.rst
.. include:: armacode/libraries/DebugVector2.rst
.. include:: armacode/libraries/DictionaryMerge.rst
.. include:: armacode/libraries/DimensionValue.rst
.. include:: armacode/libraries/DuplicateLayout.rst
.. include:: armacode/libraries/EditBox_EX.rst
.. include:: armacode/libraries/ExcelRead.rst
.. include:: armacode/libraries/ExcelReload.rst
.. include:: armacode/libraries/ExcelRun.rst
.. include:: armacode/libraries/ExplodeBlockInstance.rst
.. include:: armacode/libraries/FileIsModifiedWithin.rst
.. include:: armacode/libraries/FileOpen.rst
.. include:: armacode/libraries/GHLockAfterSolve.rst
.. include:: armacode/libraries/GHParallel.rst
.. include:: armacode/libraries/GeneratePlug.rst
.. include:: armacode/libraries/GetProjectFolder.rst
.. include:: armacode/libraries/GetRelativeFolder.rst
.. include:: armacode/libraries/GetUserText.rst
.. include:: armacode/libraries/GetUserTextAll.rst
.. include:: armacode/libraries/InspectObject.rst
.. include:: armacode/libraries/IsGHPython.rst
.. include:: armacode/libraries/IsLoaded.rst
.. include:: armacode/libraries/IsObjectInsideCurve.rst
.. include:: armacode/libraries/LayerIds.rst
.. include:: armacode/libraries/LayerProperties.rst
.. include:: armacode/libraries/LayerTruncate.rst
.. include:: armacode/libraries/LayoutDetails.rst
.. include:: armacode/libraries/LayoutProperties.rst
.. include:: armacode/libraries/LinkToObject.rst
.. include:: armacode/libraries/LinkedObject.rst
.. include:: armacode/libraries/List2DToArray2D.rst
.. include:: armacode/libraries/ListPurge.rst
.. include:: armacode/libraries/LoadConfig.rst
.. include:: armacode/libraries/Logger.rst
.. include:: armacode/libraries/MatchLayerAttributes.rst
.. include:: armacode/libraries/MatchObjectAttributes.rst
.. include:: armacode/libraries/NumberPadding.rst
.. include:: armacode/libraries/ObjectGroupList.rst
.. include:: armacode/libraries/ObjectLayer.rst
.. include:: armacode/libraries/ObjectLayerList.rst
.. include:: armacode/libraries/ObjectNameList.rst
.. include:: armacode/libraries/ObjectProperties.rst
.. include:: armacode/libraries/ObjectPropertiesMerge.rst
.. include:: armacode/libraries/ObjectReferencePoint.rst
.. include:: armacode/libraries/ObjectsByAttributes.rst
.. include:: armacode/libraries/ObjectsByLayout.rst
.. include:: armacode/libraries/ObjectsByQuery.rst
.. include:: armacode/libraries/ObjectsByUserString.rst
.. include:: armacode/libraries/ObjectsInBrep.rst
.. include:: armacode/libraries/ObjectsInClosedCurve.rst
.. include:: armacode/libraries/ObjectsInView.rst
.. include:: armacode/libraries/ObjectsSortByName.rst
.. include:: armacode/libraries/OffsetCurve.rst
.. include:: armacode/libraries/OrientObjects.rst
.. include:: armacode/libraries/ParallelRun.rst
.. include:: armacode/libraries/PlaneAlign.rst
.. include:: armacode/libraries/PlaneFromObject.rst
.. include:: armacode/libraries/PlaneFromPolyline.rst
.. include:: armacode/libraries/PlaneFromSurface.rst
.. include:: armacode/libraries/PointClosestObjects.rst
.. include:: armacode/libraries/PrintAll.rst
.. include:: armacode/libraries/PrintPDF.rst
.. include:: armacode/libraries/PrintPDFSetup.rst
.. include:: armacode/libraries/ProcessPerFile.rst
.. include:: armacode/libraries/ProgressBar.rst
.. include:: armacode/libraries/PullPolylineToObjects.rst
.. include:: armacode/libraries/RandomColor.rst
.. include:: armacode/libraries/RangeFormat.rst
.. include:: armacode/libraries/SaveFileName.rst
.. include:: armacode/libraries/ScreenShot.rst
.. include:: armacode/libraries/SelectedObjects.rst
.. include:: armacode/libraries/SetUserAttributeToObjects.rst
.. include:: armacode/libraries/SetUserText.rst
.. include:: armacode/libraries/SetUserTextFromDict.rst
.. include:: armacode/libraries/SortByIndices.rst
.. include:: armacode/libraries/SortObjectsAlongCurve.rst
.. include:: armacode/libraries/SortObjectsAlongPolyline.rst
.. include:: armacode/libraries/SortSynchronous.rst
.. include:: armacode/libraries/StickyGet.rst
.. include:: armacode/libraries/StickySet.rst
.. include:: armacode/libraries/StringFieldNames.rst
.. include:: armacode/libraries/StringFromAttributes.rst
.. include:: armacode/libraries/TextObjectTextFormula.rst
.. include:: armacode/libraries/TextObjectsByFont.rst
.. include:: armacode/libraries/TextObjectsByProperties.rst
.. include:: armacode/libraries/UnfoldBrep.rst
.. include:: armacode/libraries/UnfoldBrepAuto.rst
.. include:: armacode/libraries/UnfoldSurface.rst
.. include:: armacode/libraries/ValueRemap.rst
.. include:: armacode/libraries/VectorFromLine.rst
.. include:: armacode/libraries/ViewRadius.rst
.. include:: armacode/libraries/ViewSize.rst

