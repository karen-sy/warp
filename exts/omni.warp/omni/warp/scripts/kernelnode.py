# Copyright (c) 2022 NVIDIA CORPORATION.  All rights reserved.
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

MAX_DIMENSIONS = 4

SUPPORTED_ATTR_TYPES = (
    "bool", "bool[]",
    "color3f", "color3f[]",
    "color4f", "color4f[]",
    "double", "double[]",
    "float", "float[]",
    "float2", "float2[]",
    "float3", "float3[]",
    "float4", "float4[]",
    "int", "int[]",
    "int64", "int64[]",
    "matrix2d", "matrix2d[]",
    "matrix3d", "matrix3d[]",
    "matrix4d", "matrix4d[]",
    "normal3f", "normal3f[]",
    "point3f", "point3f[]",
    "quatf", "quatf[]",
    "timecode", "timecode[]",
    "token", "token[]",
    "uchar", "uchar[]",
    "uint", "uint[]",
    "uint64", "uint64[]",
    "vector3f", "vector3f[]",
)

ATTR_TO_WARP_TYPE = {
    "bool"       : "wp.int8",
    "bool[]"     : "wp.array(dtype=wp.int8)",
    "color3f"    : "wp.vec3",
    "color3f[]"  : "wp.array(dtype=wp.vec3)",
    "color4f"    : "wp.vec4",
    "color4f[]"  : "wp.array(dtype=wp.vec4)",
    "double"     : "wp.float64",
    "double[]"   : "wp.array(dtype=wp.float64)",
    "float"      : "wp.float32",
    "float[]"    : "wp.array(dtype=wp.float32)",
    "float2"     : "wp.vec2",
    "float2[]"   : "wp.array(dtype=wp.vec2)",
    "float3"     : "wp.vec3",
    "float3[]"   : "wp.array(dtype=wp.vec3)",
    "float4"     : "wp.vec4",
    "float4[]"   : "wp.array(dtype=wp.vec4)",
    "int"        : "wp.int32",
    "int[]"      : "wp.array(dtype=wp.int32)",
    "int64"      : "wp.int64",
    "int64[]"    : "wp.array(dtype=wp.int64)",
    "matrix2d"   : "wp.mat22",
    "matrix2d[]" : "wp.array(dtype=wp.mat22)",
    "matrix3d"   : "wp.mat33",
    "matrix3d[]" : "wp.array(dtype=wp.mat33)",
    "matrix4d"   : "wp.mat44",
    "matrix4d[]" : "wp.array(dtype=wp.mat44)",
    "normal3f"   : "wp.vec3",
    "normal3f[]" : "wp.array(dtype=wp.vec3)",
    "point3f"    : "wp.vec3",
    "point3f[]"  : "wp.array(dtype=wp.vec3)",
    "quatf"      : "wp.quat",
    "quatf[]"    : "wp.array(dtype=wp.quat)",
    "timecode"   : "wp.float32",
    "timecode[]" : "wp.array(dtype=wp.float32)",
    "token"      : "wp.uint64",
    "token[]"    : "wp.array(dtype=wp.uint64)",
    "uchar"      : "wp.uint8",
    "uchar[]"    : "wp.array(dtype=wp.uint8)",
    "uint"       : "wp.uint32",
    "uint[]"     : "wp.array(dtype=wp.uint32)",
    "uint64"     : "wp.uint64",
    "uint64[]"   : "wp.array(dtype=wp.uint64)",
    "vector3f"   : "wp.vec3",
    "vector3f[]" : "wp.array(dtype=wp.vec3)",
}

assert sorted(ATTR_TO_WARP_TYPE.keys()) == sorted(SUPPORTED_ATTR_TYPES)
