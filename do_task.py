import list_tasks

def imprimir_jsons():
    for json_data in list_tasks.tasks:
        print(json_data)

if __name__ == "__main__":
    imprimir_jsons()



