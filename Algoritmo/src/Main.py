import utilities

if __name__ == "__main__":

    # Read Instance
    instance = utilities.read_instance("instance_small.txt")
    print("Instance has been read")

    # Compute distances
    instance.compute_dist("default")
    print("Distances have been calculated")

    archivo = open("ejemplo.txt","w")
    for i in range(1,(len(instance.nodes)+1)):
        for j in range(1,(len(instance.nodes)+1)):
            archivo.write("("+str(i)+","+str(j)+") "+ str(instance.distances[(i, j)])+"\n")
    archivo.close()