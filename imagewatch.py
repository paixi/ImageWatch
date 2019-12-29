#!/usr/bin/env python3
import os
import pygame

class Image:
    def __init__(self, filename):
        self.filename = filename
        self.mtime = 0
        self.check()
    
    def check(self):
        if not os.path.exists(self.filename):
            self.surface = None
            return False
        mtime = os.stat(self.filename).st_mtime
        if mtime != self.mtime:
            self.dirty = True
            try:
                self.reload()
            except pygame.error:
                return False
            self.mtime = mtime
        return True
    
    def reload(self):
        self.surface = pygame.image.load(self.filename)    
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
    
    def draw(self, surface, pos=(0,0)):
        if self.surface != None:
            surface.blit(self.surface, pos)
        self.dirty = False

class ImageWatch:
    def __init__(self, images, caption="ImageWatch", nrow=2, framerate=5):
        self.caption = caption
        self.nrow = nrow
        self.framerate = framerate        
        self.images = []
        total_height = 0
        max_width = 0
        width = 0
        height = 0
        x = 0
        y = 0
        i = 0
        for image in images:
            if i % nrow == 0:
                x = 0
                width = 0
                y += height
                total_height += height
            img = Image(image)
            width += img.width
            if width > max_width:
                max_width = width
            if img.height > height:
                height = img.height
            self.images.append((img, (x,y)))
            x += img.width
            i += 1
        total_height += height
        size = (max_width, total_height)
        pygame.display.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(size)        
    
    def start(self):
        clock = pygame.time.Clock()
        while True:
            dirty = False
            for event in pygame.event.get():
                if event.type == pygame.VIDEOEXPOSE:
                    dirty = True
                elif event.type == pygame.QUIT:
                    raise SystemExit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        raise SystemExit
            for image, pos in self.images:
                image.check()
                dirty |= image.dirty
            if dirty:
                self.screen.fill((0,0,0))
                for image, pos in self.images:
                    image.draw(self.screen, pos)
                pygame.display.flip()
            clock.tick(self.framerate)

if __name__ == '__main__':
    from argparse import ArgumentParser
    from glob import glob
    p = ArgumentParser()
    p.add_argument("images", type=str, help="glob pathname")
    p.add_argument("--caption", "-c", type=str, default="ImageWatch", help="window caption")
    p.add_argument("--nrow", "-n", type=int, default=2, help="number of images per row")
    p.add_argument("--fps", "-f", type=int, default=5, help="update framerate")
    args = p.parse_args()
    iw = ImageWatch(glob(args.images), caption=args.caption, nrow=args.nrow, framerate=args.fps)
    iw.start()
