not mode: sleep
-
parrot(cluck):
				print("cluck")
parrot(tut):
				print("tut")
				user.on_tut()
parrot(palate_click):
				user.on_palate()
				print("on_palate")
parrot(pop):
				user.on_pop()
				# print("pop")
parrot(shush):              user.noise_debounce("shush", true)
parrot(shush:stop):         user.noise_debounce("shush", false)

parrot(hiss):               user.noise_debounce("hiss", true)
parrot(hiss:stop):          user.noise_debounce("hiss", false)
# parrot(shush):              user.noise_debounce("shush", true)
# parrot(shush:stop):         user.noise_debounce("shush", false)

# parrot(hiss):               user.noise_debounce("hiss", true)
# parrot(hiss:stop):          user.noise_debounce("hiss", false)
parrot(ue):
	# user.hud_activate_dwell_key()
				print("ue")
parrot(lll):
				print("lll")
parrot(buzz):
				print("buzz")
parrot(gluck):
				print("gluck")
# parrot(finger_snap):
# 				print("finger_snap")
parrot(ch):
				print("ch")
parrot(ah):
				print("ah")
parrot(aa):		print("aa")
parrot(oh):
				print("oh")
parrot(iy):
	# user.hud_activate_virtual_key()
	print("iy")
parrot(ae):
				print("ae")
parrot(horse):
				print("horse")
# parrot(whistle):
# 				print("whistle")
parrot(chopper):
				print("chopper")
parrot(hurr):
				print("hurr")
parrot(hmm):
				print("hmm")
parrot(oo):
				print("oo")
parrot(yee):
				print("yee")
parrot(uh):
				print("uh")
parrot(fff):
				print("fff")
parrot(generator):
				print("generator")
parrot(x):
				print("x")
