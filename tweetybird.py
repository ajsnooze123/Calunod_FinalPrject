import turtle

def draw_image(coordinates, fill_color):
    turtle.speed(0) 
    turtle.pu()  
    turtle.title("Tweety Bird")

    if coordinates:
        turtle.goto(coordinates[0]) 
        turtle.pd()  
        turtle.ht()
        turtle.fillcolor(fill_color)  
        turtle.begin_fill()  
        for coordinate in coordinates:
            x, y = coordinate
            turtle.goto(x, y)
        turtle.end_fill()  

    turtle.pu()  
    turtle.home()    
    turtle.pd() 

def draw_images_from_files(file_colors):
    for fname, fill_color in file_colors.items():
        with open(fname, 'r') as file:
            fill_color = file.readline().strip()
            fcoordinates = [tuple(map(float, line.strip().split(','))) for line in file]
            draw_image(fcoordinates, fill_color)

    turtle.done()

file_colors = {
    'coordinates/d1': 'yellow',
    'coordinates/d2': 'white',   
    'coordinates/d3': 'white',
    'coordinates/d4': 'black',
    'coordinates/d5': 'black',
    'coordinates/d6': '#FF6100',
    'coordinates/d7': '#FF6100',
    'coordinates/d8': 'blue',
    'coordinates/d9': '#009eff',
    'coordinates/o1': 'blue',
    'coordinates/o2': '#009eff',
    'coordinates/o3': 'black',
    'coordinates/o4': 'black',
    'coordinates/o5': 'black',
    'coordinates/o6': 'black',
    'coordinates/o7': 'black',
    'coordinates/o8': 'black',
    'coordinates/o9': 'black',
    'coordinates/g1': 'black',
    'coordinates/g2': 'black',
    'coordinates/g3': 'yellow',
    'coordinates/g4': "black",
    'coordinates/g5': "black",
    'coordinates/g6': "white",
    'coordinates/g7': "black",
    'coordinates/g8': "black",
    'coordinates/g9': "yellow",
    'coordinates/y1': "black",
    'coordinates/y2': "black",
    'coordinates/y3': "black",
    'coordinates/y4': "#ffa500",
    'coordinates/y5': "#ffa500",
}
draw_images_from_files(file_colors)