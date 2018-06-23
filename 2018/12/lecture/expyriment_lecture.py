from expyriment import design, control, stimuli

control.defaults.window_mode = True
control.defaults.window_size = [800,600]
design.defaults.experiment_background_colour = (230,230,70)

exp = design.Experiment(name="Cool Experiment")
control.initialize(exp)

block_one = design.Block(name="Our only block")
tmp_trial = design.Trial()

cross = stimuli.FixCross()
cross.preload()

# define stimulus positions
positions = [-400, -200, 0, 200, 400]

# go through all positions
for xpos in positions:
    # create circle accordingly
    stim = stimuli.Circle(radius=25, colour=(0,0,0),position=[xpos,0])
    stim.preload()
    tmp_trial.add_stimulus(stim)
    tmp_trial.add_stimulus(cross)
    block_one.add_trial(tmp_trial)
    tmp_trial = tmp_trial.copy()
    tmp_trial.clear_stimuli()
exp.add_block(block_one)
control.start()

for b in exp.blocks:
    for t in b.trials:
        t.stimuli[0].present(clear=True, update=False)
        t.stimuli[1].present(clear=False, update=True)

        exp.keyboard.wait()

control.end()
