import media
import fresh_tomatoes
#instances
doctor_strange =  media.Movie("Doctor Strange",
                        "A former neurosurgeon embarks on a journey of healing only to be drawn into the world of the mystic arts.",
                        "http://www.joblo.com/posters/images/full/doctor-strange-poster.jpg",
                        "https://www.youtube.com/watch?v=HSzx-zryEgM&t=22s")
#print (doctor_strange.storyline)

pirates_of_caribbean = media.Movie('Pirates of the Caribbean 5:"Dead Men Tell No Tales"',
                                  "Captain Jack Sparrow searches for the trident of Poseidon.",
                                  "https://s-media-cache-ak0.pinimg.com/564x/97/78/cd/9778cd9682807aa99e05c19d4dc2b969.jpg",
                                  "https://www.youtube.com/watch?v=w69ZgDfmKcA")
#print (pirates_of_caribbean.storyline)

guardian_of_galaxy = media.Movie("Guardians of the Galaxy 2",
                                 "Set to the backdrop of Awesome Mixtape #2, 'Guardians of the Galaxy Vol. 2' continues the team's adventures as they unravel the mystery of Peter Quill's true parentage.",
                                 "http://static.comicvine.com/uploads/original/14/142175/4327607-hulk_and_the_guardians_of_the_galaxy___movie_by_worldbreakerhulk-d8ccbya.jpg",
                                 "https://www.youtube.com/watch?v=dW1BIid8Osg")
#print (guardian_of_galaxy.storyline)

transformer = media.Movie("Transformer : The Last Knight",
                          "Humans and Transformers are at war, Optimus Prime is gone. The key to saving our future lies buried in the secrets of the past, in the hidden history of Transformers on Earth.",
                          "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",
                          "https://www.youtube.com/watch?v=AntcyqJ6brc")
#print (transformer.storyline)

power_ranger = media.Movie("Power Rangers",
                           "A group of high-school kids, who are infused with unique superpowers, harness their abilities in order to save the world.",
                           "https://s-media-cache-ak0.pinimg.com/736x/d7/2c/af/d72caf118629139bac1128346a466781.jpg",
                           "https://www.youtube.com/watch?v=Q-C4qqsgs8w")
#print (power_ranger.storyline)

smurfs = media.Movie("Smurfs: The lost Village",
                     "In this fully animated, all-new take on the Smurfs, a mysterious map sets Smurfette and her friends Brainy, Clumsy and Hefty on an exciting race through the Forbidden Forest leading to the discovery of the biggest secret in Smurf history.",
                     "https://upload.wikimedia.org/wikipedia/en/0/07/Smurfs_The_Lost_Village_poster.jpg",
                     "https://www.youtube.com/watch?v=8LdpyRBE0aA")
#print(smurfs.storyline)

despicable_me = media.Movie("Despicable Me 3",
                         "Balthazar Bratt, a child star from the 1980s, hatches a scheme for world domination.",
                         "http://www.buyminions.com/wp-content/uploads/2016/09/yayomg-despicable-me-3-768x384.jpg",
                         "https://www.youtube.com/watch?v=6DBi41reeF0")
#print(despicable_me.storyline)

movies = [doctor_strange,pirates_of_caribbean,guardian_of_galaxy,transformer,power_ranger,smurfs,despicable_me]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
                          
#doctor_strange.show_trailer()
