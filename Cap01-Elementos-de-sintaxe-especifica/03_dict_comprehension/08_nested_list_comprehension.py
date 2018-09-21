#!/usr/bin/env python3

nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}

float_dict = {outer_k: {(inner_k, float(inner_v)) for (inner_k, inner_v) in outer_v.items()}
              for(outer_k, outer_v) in nested_dict.items()}

print(float_dict)

for(outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})
nested_dict.update({outer_k:outer_v})

print(nested_dict)