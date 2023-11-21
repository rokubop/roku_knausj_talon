not mode:                   sleep
and not mode:               user.parrot
-
parrot(cluck):
	# print("cluck")
	user.parrot_mode_enable()
parrot(tut):
	# print("tut")
	user.on_tut()
parrot(palate_click):
	# print("on_palate")
	user.on_palate()
parrot(pop):
	# print("pop")
	user.on_pop()
parrot(shush):
	# print("shush")
	# user.on_shush_start()
parrot(shush:stop):
	# print("shush:stop")
	# user.on_shush_stop()
parrot(hiss):
	# print("hiss")
	# user.on_hiss_start()
parrot(hiss:stop):
	# print("hiss:stop")
	# user.on_hiss_stop()
parrot(ee):
	# print("ee")
	user.on_force_scroll_stop()
	# user.omega_mouse_left_click()
parrot(ee:stop):
	# print("ee:stop")
	# user.on_ee_stop()
parrot(ah):
	# print("ah")
	user.on_ah()
parrot(eh):
	# print("eh")
	user.on_eh()
parrot(oh):
	# print("oh")
	user.on_oh()
parrot(t): skip()
	# print("t")
parrot(er):
	# print("er")
	user.on_er()
parrot(guh):
	# print("guh")
	user.on_guh()
parrot(nn):
	# print("nn")
	user.on_nn()
