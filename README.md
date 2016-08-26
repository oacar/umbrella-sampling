# umbrella-sampling

Workflow of this class:
1- Define an umbrella with UmbrellaPotential object
2- Run an US simulation and add the trajectory to UmbrellaPotential object
3- Create an UmbrellaIterator object with UmbrellaPotential object and define an overlap
4- Until you get an accepted value, use UmbrellaIterator.center_check function and run new simulation
5- In order to calculate next umbrella position, use UmbrellaIterator.find_next_umbrella function
6- Until covering all the reaction coordinate use above steps

Known Issues:
1- If the energy barrier is very high compared to the spring constant given, program cannot return an accepted value, best approach is increasing k value if after 20 trials there is no accepted value.
