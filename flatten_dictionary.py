# Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

def flatten_dictionary(dictionary):
  flat = {}
  for key, value in dictionary.items():
    if type(value) == dict:
      result = flatten_dictionary(value)

      for k in result:
        if key != '' and k != '':
          flat[key + '.' + k] = result[k]
        elif key == '':
          flat[k] = result[k]
        elif k == '':
          flat[key] = result[k]
          
    else:
      flat[key] = value
      
  return flat


# input:  dict = {
#             "Key1" : "1",
#             "Key2" : {
#                 "a" : "2",
#                 "b" : "3",
#                 "c" : {
#                     "d" : "3",
#                     "e" : {
#                         "" : "1"
#                     }
#                 }
#             }
#         }

# output: {
#             "Key1" : "1",
#             "Key2.a" : "2",
#             "Key2.b" : "3",
#             "Key2.c.d" : "3",
#             "Key2.c.e" : "1"
#         }
