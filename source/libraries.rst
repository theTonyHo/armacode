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
   :local:

.. Include all generated documents below


.. include:: armacode/libraries/AddBlock.rst
   :start-line: 3
.. include:: armacode/libraries/AddDimAlignedFromLine.rst
   :start-line: 3
.. include:: armacode/libraries/AddDimLinearFromLine.rst
   :start-line: 3
.. include:: armacode/libraries/AddLayer.rst
   :start-line: 3
.. include:: armacode/libraries/AddLineEX.rst
   :start-line: 3
.. include:: armacode/libraries/AddLinearDimension.rst
   :start-line: 3
.. include:: armacode/libraries/AddObjectsToBlock.rst
   :start-line: 3
.. include:: armacode/libraries/AddPlaneSurfaceCenter.rst
   :start-line: 3
.. include:: armacode/libraries/AnnotationProperties.rst
   :start-line: 3
.. include:: armacode/libraries/AnnotationText.rst
   :start-line: 3
.. include:: armacode/libraries/BlockInstanceBasePlane.rst
   :start-line: 3
.. include:: armacode/libraries/BlockModify.rst
   :start-line: 3
.. include:: armacode/libraries/BlockProperties.rst
   :start-line: 3
.. include:: armacode/libraries/BrepEdgeCreaseAngle.rst
   :start-line: 3
.. include:: armacode/libraries/BrepEdges.rst
   :start-line: 3
.. include:: armacode/libraries/BrepReorderFaces.rst
   :start-line: 3
.. include:: armacode/libraries/BrepSplitWithCurves.rst
   :start-line: 3
.. include:: armacode/libraries/CSVOpen.rst
   :start-line: 3
.. include:: armacode/libraries/CSVRead.rst
   :start-line: 3
.. include:: armacode/libraries/CSVWrite.rst
   :start-line: 3
.. include:: armacode/libraries/ClearUserText.rst
   :start-line: 3
.. include:: armacode/libraries/CommonEdge.rst
   :start-line: 3
.. include:: armacode/libraries/CreaseAngle.rst
   :start-line: 3
.. include:: armacode/libraries/CurveDuplicates.rst
   :start-line: 3
.. include:: armacode/libraries/CurveSplitOverlap.rst
   :start-line: 3
.. include:: armacode/libraries/DebugArray2D.rst
   :start-line: 3
.. include:: armacode/libraries/DebugCurveDeviation.rst
   :start-line: 3
.. include:: armacode/libraries/DebugLine.rst
   :start-line: 3
.. include:: armacode/libraries/DebugValues.rst
   :start-line: 3
.. include:: armacode/libraries/DebugVector.rst
   :start-line: 3
.. include:: armacode/libraries/DebugVector2.rst
   :start-line: 3
.. include:: armacode/libraries/DictionaryMerge.rst
   :start-line: 3
.. include:: armacode/libraries/DimensionValue.rst
   :start-line: 3
.. include:: armacode/libraries/DuplicateLayout.rst
   :start-line: 3
.. include:: armacode/libraries/EditBox_EX.rst
   :start-line: 3
.. include:: armacode/libraries/ExcelRead.rst
   :start-line: 3
.. include:: armacode/libraries/ExcelReload.rst
   :start-line: 3
.. include:: armacode/libraries/ExcelRun.rst
   :start-line: 3
.. include:: armacode/libraries/ExplodeBlockInstance.rst
   :start-line: 3
.. include:: armacode/libraries/FileIsModifiedWithin.rst
   :start-line: 3
.. include:: armacode/libraries/FileOpen.rst
   :start-line: 3
.. include:: armacode/libraries/GHLockAfterSolve.rst
   :start-line: 3
.. include:: armacode/libraries/GHParallel.rst
   :start-line: 3
.. include:: armacode/libraries/GeneratePlug.rst
   :start-line: 3
.. include:: armacode/libraries/GetProjectFolder.rst
   :start-line: 3
.. include:: armacode/libraries/GetRelativeFolder.rst
   :start-line: 3
.. include:: armacode/libraries/GetUserText.rst
   :start-line: 3
.. include:: armacode/libraries/GetUserTextAll.rst
   :start-line: 3
.. include:: armacode/libraries/InspectObject.rst
   :start-line: 3
.. include:: armacode/libraries/IsGHPython.rst
   :start-line: 3
.. include:: armacode/libraries/IsLoaded.rst
   :start-line: 3
.. include:: armacode/libraries/IsObjectInsideCurve.rst
   :start-line: 3
.. include:: armacode/libraries/LayerIds.rst
   :start-line: 3
.. include:: armacode/libraries/LayerProperties.rst
   :start-line: 3
.. include:: armacode/libraries/LayerTruncate.rst
   :start-line: 3
.. include:: armacode/libraries/LayoutDetails.rst
   :start-line: 3
.. include:: armacode/libraries/LayoutProperties.rst
   :start-line: 3
.. include:: armacode/libraries/LinkToObject.rst
   :start-line: 3
.. include:: armacode/libraries/LinkedObject.rst
   :start-line: 3
.. include:: armacode/libraries/List2DToArray2D.rst
   :start-line: 3
.. include:: armacode/libraries/ListPurge.rst
   :start-line: 3
.. include:: armacode/libraries/LoadConfig.rst
   :start-line: 3
.. include:: armacode/libraries/Logger.rst
   :start-line: 3
.. include:: armacode/libraries/MatchLayerAttributes.rst
   :start-line: 3
.. include:: armacode/libraries/MatchObjectAttributes.rst
   :start-line: 3
.. include:: armacode/libraries/NumberPadding.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectGroupList.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectLayer.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectLayerList.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectNameList.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectProperties.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectPropertiesMerge.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectReferencePoint.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsByAttributes.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsByLayout.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsByQuery.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsByUserString.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsInBrep.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsInClosedCurve.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsInView.rst
   :start-line: 3
.. include:: armacode/libraries/ObjectsSortByName.rst
   :start-line: 3
.. include:: armacode/libraries/OffsetCurve.rst
   :start-line: 3
.. include:: armacode/libraries/OrientObjects.rst
   :start-line: 3
.. include:: armacode/libraries/ParallelRun.rst
   :start-line: 3
.. include:: armacode/libraries/PlaneAlign.rst
   :start-line: 3
.. include:: armacode/libraries/PlaneFromObject.rst
   :start-line: 3
.. include:: armacode/libraries/PlaneFromPolyline.rst
   :start-line: 3
.. include:: armacode/libraries/PlaneFromSurface.rst
   :start-line: 3
.. include:: armacode/libraries/PointClosestObjects.rst
   :start-line: 3
.. include:: armacode/libraries/PrintAll.rst
   :start-line: 3
.. include:: armacode/libraries/PrintPDF.rst
   :start-line: 3
.. include:: armacode/libraries/PrintPDFSetup.rst
   :start-line: 3
.. include:: armacode/libraries/ProcessPerFile.rst
   :start-line: 3
.. include:: armacode/libraries/ProgressBar.rst
   :start-line: 3
.. include:: armacode/libraries/PullPolylineToObjects.rst
   :start-line: 3
.. include:: armacode/libraries/RandomColor.rst
   :start-line: 3
.. include:: armacode/libraries/RangeFormat.rst
   :start-line: 3
.. include:: armacode/libraries/SaveFileName.rst
   :start-line: 3
.. include:: armacode/libraries/ScreenShot.rst
   :start-line: 3
.. include:: armacode/libraries/SelectedObjects.rst
   :start-line: 3
.. include:: armacode/libraries/SetUserAttributeToObjects.rst
   :start-line: 3
.. include:: armacode/libraries/SetUserText.rst
   :start-line: 3
.. include:: armacode/libraries/SetUserTextFromDict.rst
   :start-line: 3
.. include:: armacode/libraries/SortByIndices.rst
   :start-line: 3
.. include:: armacode/libraries/SortObjectsAlongCurve.rst
   :start-line: 3
.. include:: armacode/libraries/SortObjectsAlongPolyline.rst
   :start-line: 3
.. include:: armacode/libraries/SortSynchronous.rst
   :start-line: 3
.. include:: armacode/libraries/StickyGet.rst
   :start-line: 3
.. include:: armacode/libraries/StickySet.rst
   :start-line: 3
.. include:: armacode/libraries/StringFieldNames.rst
   :start-line: 3
.. include:: armacode/libraries/StringFromAttributes.rst
   :start-line: 3
.. include:: armacode/libraries/TextObjectTextFormula.rst
   :start-line: 3
.. include:: armacode/libraries/TextObjectsByFont.rst
   :start-line: 3
.. include:: armacode/libraries/TextObjectsByProperties.rst
   :start-line: 3
.. include:: armacode/libraries/UnfoldBrep.rst
   :start-line: 3
.. include:: armacode/libraries/UnfoldBrepAuto.rst
   :start-line: 3
.. include:: armacode/libraries/UnfoldSurface.rst
   :start-line: 3
.. include:: armacode/libraries/ValueRemap.rst
   :start-line: 3
.. include:: armacode/libraries/VectorFromLine.rst
   :start-line: 3
.. include:: armacode/libraries/ViewRadius.rst
   :start-line: 3
.. include:: armacode/libraries/ViewSize.rst
   :start-line: 3

