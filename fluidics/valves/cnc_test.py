import cnc_talk

cnc = cnc_talk.CNC()
plate = cnc_talk.Plate(cnc)

print("plate.positions: ")
print(plate.positions)

plate.record_well()
cnc.set((0, 0, 0))

print("\nplate.positions: ")
print(plate.positions)


plate.record_well(8, 12)
cnc.set((8, 12, 20))
plate.record_height()

plate.record_well(8, 0)
cnc.set((8, 0, 20))
plate.record_height()

print("\nplate.positions: ")
print(plate.positions)

plate.freeze()
cnc.set((4, 4, 0))
plate.record_well(4,4)
cnc.set((0, 12, 0))
plate.record_well(0, 12)
cnc.set((8, 0, 0))
plate.record_well(8, 0)
plate.freeze()

print("\n\n\n!!!\n\n\n")

plate.move(x=8, y=8)
print("8,8")
plate.move(x=0, y=0)
plate.move(x=4, y=0)