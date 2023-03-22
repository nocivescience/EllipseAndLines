from manim import *
class CurveMoving(Scene):
    conf={
        't_offset':0,
        'rate':2,
        'radio':.02
    }
    def construct(self):
        axes=Axes()
        dot=self.get_dot()
        circle=Circle(radius=2.5).fade(1)
        circle.dot=dot
        dots=self.get_dots(circle)
        dots.dot=dot
        dots.add_updater(self.get_lines_update)
        for mob in [axes,dot,dots,circle,dots.Lines]:
            self.add(mob)
        self.wait(14)
    def get_dot(self):
        dot =Dot(radius=self.conf['radio']).move_to(
            2.5*np.array([np.cos(0),np.sin(0),0])
        )
        dot.add_updater(self.get_update_dot)
        return dot
    def get_update_dot(self,mob,dt):
        rate=dt*self.conf['rate']
        mob.move_to(2.501*np.array([np.cos(rate+self.conf['t_offset']),np.sin(rate+self.conf['t_offset']),0]))
        self.conf['t_offset']+=rate
    def get_dots(self,curve):
        Dots=VGroup()
        Lines=VGroup()
        for t in np.linspace(0,1,50):
            dot=Dot(radius=self.conf['radio']).move_to(
                curve.point_from_proportion(t)
            )
            line=Line(curve.dot,dot,stroke_width=2)
            Dots.add(dot)
            Lines.add(line)
            Dots.Lines=Lines
        return Dots
    def get_lines_update(self,dots):
        for dot,line in zip(dots,dots.Lines):
            line.put_start_and_end_on(
                dots.dot.get_center(),dot.get_center()
            )