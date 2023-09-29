from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand=load_image('hand_arrow.png')

def handle_events():
    global running
    global handx, handy,clicky,clickx,clickcount
    global beforey,beforex,i

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            handx, handy = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type==SDL_MOUSEBUTTONDOWN:
            clickx.append(event.x)
            clicky.append(TUK_HEIGHT - 1 - event.y)
            clickcount+=1




running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
handx, handy = TUK_WIDTH // 2, TUK_HEIGHT // 2
clickx= []
clicky =[]
clickcount=0
count=0
frame = 0
hide_cursor()
i=0
beforex=[x]
beforey=[y]
movetime=0
subhand=0
while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if clickcount>0 and clickcount>count:
        if movetime % 10 == 0:
            t = i / 100
            x = (1 - t) * beforex[count] + t * clickx[count]
            y = (1 - t) * beforey[count] + t * clicky[count]
            i += 1
            if i > 100:
                beforex.append(clickx[count])
                beforey.append(clicky[count])
                subhand+=1
                count+=1
                i=0
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    for j in range(subhand,clickcount):
        hand.draw(clickx[j],clicky[j])
    hand.draw(handx, handy)
    update_canvas()
    frame = (frame + 1) % 8
    movetime+=1
    handle_events()

close_canvas()




