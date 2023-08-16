not mode:                   sleep
-
parrot(cluck):
	print("cluck")
parrot(tut):
	print("tut")
	user.on_tut()
parrot(palate_click):
	print("on_palate")
	user.on_palate()
parrot(pop):
	user.on_pop()
parrot(bup):
	print("bup")
parrot(shush):              user.noise_debounce("shush", true)
parrot(shush:stop):         user.noise_debounce("shush", false)

parrot(hiss):               user.noise_debounce("hiss", true)
parrot(hiss:stop):          user.noise_debounce("hiss", false)
parrot(ah):
	print("ah")
parrot(oh):
	print("oh")
parrot(iy):
	print("iy")
	# user.hud_activate_virtual_key()


# parrot(ue):
# 	print("ue")
# parrot(lll):
# 	print("lll")
# parrot(buzz):
# 	print("buzz")
# parrot(gluck):
# 	print("gluck")
# # parrot(finger_snap):
# # 				print("finger_snap")
# parrot(ch):
# 	print("ch")
# parrot(aa):                 print("aa")
# parrot(ae):
# 	print("ae")
# parrot(horse):
# 	print("horse")
# parrot(whistle):
# 				print("whistle")
# parrot(chopper):
# 	print("chopper")
# parrot(hurr):
# 	print("hurr")
# parrot(hmm):
# 	print("hmm")
# parrot(oo):
# 	print("oo")
# parrot(yee):
# 	print("yee")
# parrot(uh):
# 	print("uh")
# parrot(fff):
# 	print("fff")
# parrot(generator):
# 	print("generator")
# parrot(x):
# 	print("x")
