from psychopy import visual, event, core, data

mywin = visual.Window(size=[800,600], monitor="testMonitor", units="norm", color=[255,255,0])

positions = (-1, -0.5, 0, 0.5, 1)
handler = data.TrialHandler(positions, 1, method='sequential')

fixation = visual.GratingStim(win=mywin, size=0.015, pos=[0,0], sf=0, color=-1)
grating = visual.GratingStim(win=mywin, mask="circle", size=0.2, pos=[0,0], sf=3)

event.globalKeys.add(key='escape', func=core.quit)

for trial in handler:
    grating.setPos([trial,0])
    fixation.draw()
    grating.draw()
    mywin.flip()
    while(event.waitKeys() == None):
        print('hihi')
