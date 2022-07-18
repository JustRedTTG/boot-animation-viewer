import os
import pgerom as pe
pe.init()
aspect = 20
pe.display.make((int(9*aspect), int(19.5*aspect)),'boot animation viewer')
def togif(folder, size=(1,1)):
    size = list(size)
    images = []
    position = [0,0]
    if size[0] > int(9*aspect):
        size[1] /= size[0]
        size[0] = int(9*aspect)
        size[1] *= size[0]
        size = [int(size[0]), int(size[1])]
        position[1] = int(int(19.5*aspect)/2-size[1]/2)
    def part(id,custom=False):
        print('part',id)
        skip = False
        if custom:
            images2 = []
        try:
            for _, _, files in os.walk(folder + '/part' + str(int(id)-1)):
                pass
            file = files[len(files)-4]
            image = pe.image(folder+'/part'+str(int(id)-1)+'/'+file, size, position)
            if custom:
                images2.append(image)
            else:
                images.append(image)
            skip = not skip
        except:
            print('skip double')
        for _, _, files in os.walk(folder+'/part'+id):
            pass
        for file in files:
            #print(folder+'/part'+id+'/'+file)
            if skip:
                skip = not skip
                continue
            skip = not skip
            image = pe.image(folder+'/part'+id+'/'+file, size, position)
            if custom:
                images2.append(image)
            else:
                images.append(image)
        if custom:
            return images2
        return
    part('1')
    images2 = part('2',True)
    for i in range(10):
        for image in images2:
            images.append(image)
    part('3')
    #for i in range(60):
    #    images.append(images[len(images)-1])
    print(len(images)-1)
    return images

images = togif('boot',(982,1080))
i = 0
while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    try:
        images[i].display()
        pe.display.update()
    except:
        pe.fill.full(pe.color.gray)
        pe.display.update()
    pe.time.tick(30)
    i+=1
