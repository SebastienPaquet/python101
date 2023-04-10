#empty dictionary
empty_dict = {}
print( list(globals().items())[-1] )

dict_movie_info = {
     "title": "Scarface"
    ,"lead_actor": "Al Pacino"
}
print( list(globals().items())[-1] )

#append
dict_movie_info.update({"release_year":1980})
print(dict_movie_info)

print(dict_movie_info.pop("lead_actor"))
key_to_remove = "producer"
print(dict_movie_info.pop(key_to_remove,f"{key_to_remove} is a missing_key"))
print(   dict_movie_info.pop(  key_to_remove,' '.join( str(i) for i in [key_to_remove, "is a missing_key"] )  )   )
#print(dict_movie_info.pop(key_to_remove,[list(globals().items())[-1],"is a missing_key"]))

student_grade = {"Rolf": 96, "Bob": 80, "Anne": 100}
print(student_grade.items().mapping)

#dictionary comprehension
