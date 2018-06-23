from expyriment import design, control, stimuli

control.defaults.window_mode = True
control.defaults.window_size = [800,600]
design.defaults.experiment_background_colour = (230,230,70)

exp = design.Experiment(name="Cool Experiment")

control.initialize(exp)

block_one = design.Block("Our only block")
tmp_trial = design.Trial()

cross = stimuli.FixCross(colour=(0,0,0))
cross.preload()

tmp_trial.add_stimulus(cross)
block_one.add_trial(tmp_trial)
exp.add_block(block_one)

control.start()

for b in exp.blocks:
    for t in b.trials:
        t.stimuli[0].present()

        exp.keyboard.wait()


control.end()
