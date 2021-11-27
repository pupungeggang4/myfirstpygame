import sys
import pygame

import img
import var

import start

import title
import field

clock = pygame.time.Clock()

def init():
    var.screen = pygame.display.set_mode((1280, 800))
    pygame.display.set_caption('Dessert Card RPG')
    img.image_load()
    start.start_title()

def main():
    while True:
        clock.tick(var.FPS)
        manage()
        input_handle()

def manage():
    if var.scene == 'title':
        title.manage()

    elif var.scene == 'field':
        field.manage()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        else:
            if event.type == pygame.MOUSEBUTTONUP:
                if var.scene == 'title':
                    title.mouse_up_handle()

                elif var.scene == 'field':
                    field.mouse_up_handle()

            if var.Input.Keyboard.enabled == True:
                if event.type == pygame.KEYDOWN:
                    var.Input.Keyboard.key = event.key

                    if var.Input.Keyboard.key_press == -1:
                        var.Input.Keyboard.key_press = event.key

                    if var.scene == 'field':
                        field.key_down_handle()

                elif event.type == pygame.KEYUP:
                    var.Input.Keyboard.key_press = -1 

init()
main()
