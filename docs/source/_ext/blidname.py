from docutils import nodes
from docutils.parsers.rst import Directive, directives

LINKS = {
'FunctionNodeAlignEulerToVector'           : ('Align Euler to Vector'       , 'utilities/align_euler_to_vector'),
'FunctionNodeBooleanMath'                  : ('Boolean Math'                , 'utilities/boolean_math'),
'FunctionNodeCompare'                      : ('Compare'                     , 'utilities/compare'),
'FunctionNodeFloatToInt'                   : ('Float to Integer'            , 'utilities/float_to_integer'),
'FunctionNodeInputBool'                    : ('Boolean'                     , 'input/boolean'),
'FunctionNodeInputColor'                   : ('Color'                       , 'input/color'),
'FunctionNodeInputInt'                     : ('Integer'                     , 'input/integer'),
'FunctionNodeInputSpecialCharacters'       : ('Special Characters'          , 'text/special_characters'),
'FunctionNodeInputString'                  : ('String'                      , 'input/string'),
'FunctionNodeInputVector'                  : ('Vector'                      , 'input/vector'),
'FunctionNodeRandomValue'                  : ('Random Value'                , 'utilities/random_value'),
'FunctionNodeReplaceString'                : ('Replace String'              , 'text/replace_string'),
'FunctionNodeRotateEuler'                  : ('Rotate Euler'                , 'utilities/rotate_euler'),
'FunctionNodeSliceString'                  : ('Slice String'                , 'text/slice_string'),
'FunctionNodeStringLength'                 : ('String Length'               , 'text/string_length'),
'FunctionNodeValueToString'                : ('Value to String'             , 'text/value_to_string'),
'GeometryNodeAccumulateField'              : ('Accumulate Field'            , 'utilities/accumulate_field'),
'GeometryNodeAttributeDomainSize'          : ('Domain Size'                 , 'attribute/domain_size'),
'GeometryNodeAttributeStatistic'           : ('Attribute Statistic'         , 'attribute/attribute_statistic'),
'GeometryNodeAttributeTransfer'            : ('Transfer Attribute'          , 'attribute/transfer_attribute'),
'GeometryNodeBoundBox'                     : ('Bounding Box'                , 'geometry/bounding_box'),
'GeometryNodeCaptureAttribute'             : ('Capture Attribute'           , 'attribute/capture_attribute'),
'GeometryNodeCollectionInfo'               : ('Collection Info'             , 'input/collection_info'),
'GeometryNodeConvexHull'                   : ('Convex Hull'                 , 'geometry/convex_hull'),
'GeometryNodeCurveArc'                     : ('Arc'                         , 'curve_primitives/arc'),
'GeometryNodeCurveEndpointSelection'       : ('Endpoint Selection'          , 'curve/endpoint_selection'),
'GeometryNodeCurveHandleTypeSelection'     : ('Handle Type Selection'       , 'curve/handle_type_selection'),
'GeometryNodeCurveLength'                  : ('Curve Length'                , 'curve/curve_length'),
'GeometryNodeCurvePrimitiveBezierSegment'  : ('Bezier Segment'              , 'curve_primitives/bezier_segment'),
'GeometryNodeCurvePrimitiveCircle'         : ('Curve Circle'                , 'curve_primitives/curve_circle'),
'GeometryNodeCurvePrimitiveLine'           : ('Curve Line'                  , 'curve_primitives/curve_line'),
'GeometryNodeCurvePrimitiveQuadrilateral'  : ('Quadrilateral'               , 'curve_primitives/quadrilateral'),
'GeometryNodeCurveQuadraticBezier'         : ('Quadratic Bezier'            , 'curve_primitives/quadratic_bezier'),
'GeometryNodeCurveSetHandles'              : ('Set Handle Type'             , 'curve/set_handle_type'),
'GeometryNodeCurveSpiral'                  : ('Spiral'                      , 'curve_primitives/curve_spiral'),
'GeometryNodeCurveSplineType'              : ('Set Spline Type'             , 'curve/set_spline_type'),
'GeometryNodeCurveStar'                    : ('Star'                        , 'curve_primitives/star'),
'GeometryNodeCurveToMesh'                  : ('Curve to Mesh'               , 'curve/curve_to_mesh'),
'GeometryNodeCurveToPoints'                : ('Curve to Points'             , 'curve/curve_to_points'),
'GeometryNodeDeleteGeometry'               : ('Delete Geometry'             , 'geometry/delete_geometry'),
'GeometryNodeDistributePointsOnFaces'      : ('Distribute Points on Faces'  , 'point/distribute_points_on_faces'),
'GeometryNodeDualMesh'                     : ('Dual Mesh'                   , 'mesh/dual_mesh'),
'GeometryNodeDuplicateElements'            : ('Duplicate Elements'          , 'geometry/duplicate_elements'),
'GeometryNodeExtrudeMesh'                  : ('Extrude Mesh'                , 'mesh/extrude_mesh'),
'GeometryNodeFieldAtIndex'                 : ('Field at Index'              , 'utilities/field_at_index'),
'GeometryNodeFillCurve'                    : ('Fill Curve'                  , 'curve/fill_curve'),
'GeometryNodeFilletCurve'                  : ('Fillet Curve'                , 'curve/fillet_curve'),
'GeometryNodeFlipFaces'                    : ('Flip Faces'                  , 'mesh/flip_faces'),
'GeometryNodeGeometryToInstance'           : ('Geometry to Instance'        , 'geometry/geometry_to_instance'),
'GeometryNodeGroup'                        : ('Group'                       , 'group'),
'GeometryNodeImageTexture'                 : ('Image Texture'               , 'texture/image'),
'GeometryNodeInputCurveHandlePositions'    : ('Curve Handle Positions'      , 'curve/curve_handle_position'),
'GeometryNodeInputCurveTilt'               : ('Curve Tilt'                  , 'curve/curve_tilt'),
'GeometryNodeInputID'                      : ('ID'                          , 'input/id'),
'GeometryNodeInputIndex'                   : ('Index'                       , 'input/input_index'),
'GeometryNodeInputMaterial'                : ('Material'                    , 'input/material'),
'GeometryNodeInputMaterialIndex'           : ('Material Index'              , 'material/material_index'),
'GeometryNodeInputMeshEdgeAngle'           : ('Edge Angle'                  , 'mesh/edge_angle'),
'GeometryNodeInputMeshEdgeNeighbors'       : ('Edge Neighbors'              , 'mesh/edge_neighbors'),
'GeometryNodeInputMeshEdgeVertices'        : ('Edge Vertices'               , 'mesh/edge_vertices'),
'GeometryNodeInputMeshFaceArea'            : ('Face Area'                   , 'mesh/face_area'),
'GeometryNodeInputMeshFaceIsPlanar'        : ('Face is Planar'              , 'mesh/face_is_planar'),
'GeometryNodeInputMeshFaceNeighbors'       : ('Face Neighbors'              , 'mesh/face_neighbors'),
'GeometryNodeInputMeshIsland'              : ('Mesh Island'                 , 'mesh/mesh_island'),
'GeometryNodeInputMeshVertexNeighbors'     : ('Vertex Neighbors'            , 'mesh/vertex_neighbors'),
'GeometryNodeInputNamedAttribute'          : ('Named Attribute'             , 'input/named_attribute'),
'GeometryNodeInputNormal'                  : ('Normal'                      , 'input/normal'),
'GeometryNodeInputPosition'                : ('Position'                    , 'input/position'),
'GeometryNodeInputRadius'                  : ('Radius'                      , 'input/radius'),
'GeometryNodeInputSceneTime'               : ('Scene Time'                  , 'input/scene_time'),
'GeometryNodeInputShadeSmooth'             : ('Is Shade Smooth'             , 'mesh/is_shade_smooth'),
'GeometryNodeInputSplineCyclic'            : ('Is Spline Cyclic'            , 'curve/is_spline_cyclic'),
'GeometryNodeInputSplineResolution'        : ('Spline Resolution'           , 'curve/spline_resolution'),
'GeometryNodeInputTangent'                 : ('Curve Tangent'               , 'curve/curve_tangent'),
'GeometryNodeInstanceOnPoints'             : ('Instance on Points'          , 'instances/instance_on_points'),
'GeometryNodeInstancesToPoints'            : ('Instances to Points'         , 'instances/instances_to_points'),
'GeometryNodeIsViewport'                   : ('Is Viewport'                 , 'input/is_viewport'),
'GeometryNodeJoinGeometry'                 : ('Join Geometry'               , 'geometry/join_geometry'),
'GeometryNodeMaterialSelection'            : ('Material Selection'          , 'material/material_selection'),
'GeometryNodeMergeByDistance'              : ('Merge by Distance'           , 'geometry/merge_by_distance'),
'GeometryNodeMeshBoolean'                  : ('Mesh Boolean'                , 'mesh/mesh_boolean'),
'GeometryNodeMeshCircle'                   : ('Mesh Circle'                 , 'mesh_primitives/mesh_circle'),
'GeometryNodeMeshCone'                     : ('Cone'                        , 'mesh_primitives/cone'),
'GeometryNodeMeshCube'                     : ('Cube'                        , 'mesh_primitives/cube'),
'GeometryNodeMeshCylinder'                 : ('Cylinder'                    , 'mesh_primitives/cylinder'),
'GeometryNodeMeshGrid'                     : ('Grid'                        , 'mesh_primitives/grid'),
'GeometryNodeMeshIcoSphere'                : ('Ico Sphere'                  , 'mesh_primitives/icosphere'),
'GeometryNodeMeshLine'                     : ('Mesh Line'                   , 'mesh_primitives/mesh_line'),
'GeometryNodeMeshToCurve'                  : ('Mesh to Curve'               , 'mesh/mesh_to_curve'),
'GeometryNodeMeshToPoints'                 : ('Mesh to Points'              , 'mesh/mesh_to_points'),
'GeometryNodeMeshUVSphere'                 : ('UV Sphere'                   , 'mesh_primitives/uv_sphere'),
'GeometryNodeObjectInfo'                   : ('Object Info'                 , 'input/object_info'),
'GeometryNodePointsToVertices'             : ('Points to Vertices'          , 'point/points_to_vertices'),
'GeometryNodePointsToVolume'               : ('Points to Volume'            , 'point/points_to_volume'),
'GeometryNodeProximity'                    : ('Geometry Proximity'          , 'geometry/geometry_proximity'),
'GeometryNodeRaycast'                      : ('Raycast'                     , 'geometry/raycast'),
'GeometryNodeRealizeInstances'             : ('Realize Instances'           , 'instances/realize_instances'),
'GeometryNodeRemoveAttribute'              : ('Remove Named Attribute'      , 'attribute/remove_named_attribute'),
'GeometryNodeReplaceMaterial'              : ('Replace Material'            , 'material/replace_material'),
'GeometryNodeResampleCurve'                : ('Resample Curve'              , 'curve/resample_curve'),
'GeometryNodeReverseCurve'                 : ('Reverse Curve'               , 'curve/reverse_curve'),
'GeometryNodeRotateInstances'              : ('Rotate Instances'            , 'instances/rotate_instances'),
'GeometryNodeSampleCurve'                  : ('Sample Curve'                , 'curve/sample_curve'),
'GeometryNodeScaleElements'                : ('Scale Elements'              , 'mesh/scale_elements'),
'GeometryNodeScaleInstances'               : ('Scale Instances'             , 'instances/scale_instances'),
'GeometryNodeSeparateComponents'           : ('Separate Components'         , 'geometry/separate_components'),
'GeometryNodeSeparateGeometry'             : ('Separate Geometry'           , 'geometry/separate_geometry'),
'GeometryNodeSetCurveHandlePositions'      : ('Set Handle Positions'        , 'curve/set_handle_positions'),
'GeometryNodeSetCurveRadius'               : ('Set Curve Radius'            , 'curve/set_curve_radius'),
'GeometryNodeSetCurveTilt'                 : ('Set Curve Tilt'              , 'curve/set_curve_tilt'),
'GeometryNodeSetID'                        : ('Set ID'                      , 'geometry/set_id'),
'GeometryNodeSetMaterial'                  : ('Set Material'                , 'material/set_material'),
'GeometryNodeSetMaterialIndex'             : ('Set Material Index'          , 'material/set_material_index'),
'GeometryNodeSetPointRadius'               : ('Set Point Radius'            , 'point/set_point_radius'),
'GeometryNodeSetPosition'                  : ('Set Position'                , 'geometry/set_position'),
'GeometryNodeSetShadeSmooth'               : ('Set Shade Smooth'            , 'mesh/set_shade_smooth'),
'GeometryNodeSetSplineCyclic'              : ('Set Spline Cyclic'           , 'curve/set_spline_cyclic'),
'GeometryNodeSetSplineResolution'          : ('Set Spline Resolution'       , 'curve/set_spline_resolution'),
'GeometryNodeSplineLength'                 : ('Spline Length'               , 'curve/spline_length'),
'GeometryNodeSplineParameter'              : ('Spline Parameter'            , 'curve/spline_parameter'),
'GeometryNodeSplitEdges'                   : ('Split Edges'                 , 'mesh/split_edges'),
'GeometryNodeStoreNamedAttribute'          : ('Store Named Attribute'       , 'attribute/store_named_attribute'),
'GeometryNodeStringJoin'                   : ('Join Strings'                , 'text/join_strings'),
'GeometryNodeStringToCurves'               : ('String to Curves'            , 'text/string_to_curves'),
'GeometryNodeSubdivideCurve'               : ('Subdivide Curve'             , 'curve/subdivide_curve'),
'GeometryNodeSubdivideMesh'                : ('Subdivide Mesh'              , 'mesh/subdivide_mesh'),
'GeometryNodeSubdivisionSurface'           : ('Subdivision Surface'         , 'mesh/subdivision_surface'),
'GeometryNodeSwitch'                       : ('Switch'                      , 'utilities/switch'),
'GeometryNodeTransform'                    : ('Transform'                   , 'geometry/transform'),
'GeometryNodeTranslateInstances'           : ('Translate Instances'         , 'instances/translate_instances'),
'GeometryNodeTriangulate'                  : ('Triangulate'                 , 'mesh/triangulate'),
'GeometryNodeTrimCurve'                    : ('Trim Curve'                  , 'curve/trim_curve'),
'GeometryNodeViewer'                       : ('Viewer'                      , 'output/viewer'),
'GeometryNodeVolumeToMesh'                 : ('Volume to Mesh'              , 'volume/volume_to_mesh'),
'NodeFrame'                                : ('Frame'                       , 'undef'),
'NodeGroupInput'                           : ('Group Input'                 , 'undef'),
'NodeGroupOutput'                          : ('Group Output'                , 'undef'),
'NodeReroute'                              : ('Reroute'                     , 'undef'),
'ShaderNodeClamp'                          : ('Clamp'                       , 'utilities/clamp'),
'ShaderNodeCombineRGB'                     : ('Combine RGB'                 , 'color/combine_rgb'),
'ShaderNodeCombineXYZ'                     : ('Combine XYZ'                 , 'vector/combine_xyz'),
'ShaderNodeFloatCurve'                     : ('Float Curve'                 , 'utilities/float_curve'),
'ShaderNodeMapRange'                       : ('Map Range'                   , 'utilities/map_range'),
'ShaderNodeMath'                           : ('Math'                        , 'utilities/math'),
'ShaderNodeMixRGB'                         : ('Mix'                         , 'color/mix_rgb'),
'ShaderNodeRGBCurve'                       : ('RGB Curves'                  , 'color/rgb_curves'),
'ShaderNodeSeparateRGB'                    : ('Separate RGB'                , 'color/separate_rgb'),
'ShaderNodeSeparateXYZ'                    : ('Separate XYZ'                , 'vector/separate_xyz'),
'ShaderNodeTexBrick'                       : ('Brick Texture'               , 'texture/brick'),
'ShaderNodeTexChecker'                     : ('Checker Texture'             , 'texture/checker'),
'ShaderNodeTexGradient'                    : ('Gradient Texture'            , 'texture/gradient'),
'ShaderNodeTexMagic'                       : ('Magic Texture'               , 'texture/magic'),
'ShaderNodeTexMusgrave'                    : ('Musgrave Texture'            , 'texture/musgrave'),
'ShaderNodeTexNoise'                       : ('Noise Texture'               , 'texture/noise'),
'ShaderNodeTexVoronoi'                     : ('Voronoi Texture'             , 'texture/voronoi'),
'ShaderNodeTexWave'                        : ('Wave Texture'                , 'texture/wave'),
'ShaderNodeTexWhiteNoise'                  : ('White Noise Texture'         , 'texture/white_noise'),
'ShaderNodeValToRGB'                       : ('ColorRamp'                   , 'color/color_ramp'),
'ShaderNodeValue'                          : ('Value'                       , 'input/value'),
'ShaderNodeVectorCurve'                    : ('Vector Curves'               , 'vector/vector_curves'),
'ShaderNodeVectorMath'                     : ('Vector Math'                 , 'vector/vector_math'),
'ShaderNodeVectorRotate'                   : ('Vector Rotate'               , 'vector/vector_rotate'),
}



def blender_python_ref_OLD():
    return f"https://docs.blender.org/api/current/bpy.types.{self.bl_idname}.html"

def blender_ref_OLD():
    return f"https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/{NODES_MENU[self.blender_ref_name][1]}.html"



class Blidname(Directive):
    
    has_content = True
    
    def run(self):
        
        blid = self.content[0].strip()
        
        para = nodes.subscript(text="Blender reference : ")

        text = f"{blid}, "
        api_url = f"https://docs.blender.org/api/current/bpy.types.{self.content[0]}.html"
        
        refnode = nodes.reference('', '', internal=False, refuri=api_url)
        innernode = nodes.emphasis(text, text)
        refnode.append(innernode)
        para += refnode
        
        node_name = LINKS[blid][0]
        node_ref  = LINKS[blid][1]
        
        text = f"Node '{node_name}'"
        api_url = f"https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/{node_ref}.html"

        refnode = nodes.reference('', '', internal=False, refuri=api_url)
        innernode = nodes.emphasis(text, text)
        refnode.append(innernode)
        para += refnode
        
        para += nodes.paragraph('')
        
        return [para]




def setup(app):

    app.add_directive("blid", Blidname)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }