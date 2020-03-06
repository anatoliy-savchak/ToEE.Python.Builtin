class PyDice(object):
	def __init__(self):
		self.number = 1	#	GetCount
		self.size = 1		#	GetSides
		self.bonus = 1	#	GetModifier
		return

class PySpell(object):
	def __init__(self):
		self.spell = 1	
		return

class PyObjHandle(object):
	"""Mobile object"""

	def __init__(self):
		self.area = 1	#	Gets the id of the current area, which is based on the current map.
		self.char_classes = ("first_class_name", "second_class_name")	#	a tuple containing the character classes array
		self.highest_arcane_class = 1	#	Highest Arcane spell casting class
		self.highest_divine_class = 1	#	Highest Divine spell casting class
		self.highest_arcane_caster_level = 1	#	Highest Arcane caster level
		self.highest_divine_caster_level = 1	#	Highest Divine caster level
		self.description = ""	#	Gets description display name
		self.name = 1	#	GetNameId
		self.location = 9223372036854775807	#	Gets location LongLong
		self.location_full	= object()	#	Gets location LocAndOffsets
		self.type = obj_t_npc	#	Gets obj_f type like obj_t_npc
		self.radius = 1.1	#	Gets and Sets radius
		self.height = 1.1	#	Gets and Sets RenderHeight double
		self.rotation = 1.1	#	Gets and Sets rotation double
		self.map = 1	#	Gets current map id
		self.hit_dice = PyDice()	#	Gets GetHitDice
		self.hit_dice_num = 1	#	Gets GetHitDiceNum
		self.get_size = 1	#	Gets GetSize
		self.off_x = 1.1	#	Gets GetOffsetX double
		self.off_y = 1.1	#	Gets GetOffsetY double
		#	Gets and Sets obj_script[38] = 1234
		#self.scripts = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A]	
		self.scripts = PyObjScripts()
		self.origin= 1	#	GetOriginMapId	SetOriginMapId
		if (1 == 2):
			self.substitute_inventory = PyObjHandle()	#	Gets and Sets object inventory substitute
		self.factions = [0, 1]	#	Gets object factions tuple
		self.feats = [0, 1]	#	Gets object feats tuple
		self.spells_known = [PySpell(), PySpell()]	#	Gets spells known
		self.spells_memorized = [PySpell(), PySpell()]	#	Gets spells memorized
		self.loots = 1	#	Gets and Sets LootBehaviour
		self.proto = 1	#	GetProtoId

		#helpers
		self.__state = "(2, (1880286368, 14202, 17600, (132, 111, 66, 228, 212, 83, 245, 5)))"
		return

	def __getstate__(self):
		return self.__state

	def __reduce__(self):
		pickledValue = __getstate__(self)
		return [PyObjHandle, None, pickledValue]
	
	def __setstate__(self, pickledData):
		self.__state = pickledData
		return

	def add_to_initiative(self):
		""" Adds self to initiative (combat). pc.add_to_initiative() -> none"""
		return

	def ai_flee_add(self):
		""" Adds self to flee from target. npc.ai_flee_add(PyObjHandle: target) -> none"""
		return

	def ai_follower_add(self):
		""" Adds follower to pc. pc.ai_follower_add(PyObjHandle: follower) -> int"""
		return 0

	def ai_follower_remove(self):
		""" Do not use!"""
		return 0

	def ai_follower_atmax(self):
		""" Do not use!"""
		return 0

	def ai_shitlist_add(self):
		""" 0x1005CC10::NpcAiListAppend. Probably favored enemy?"""
		return 0

	def ai_shitlist_remove(self):
		""" Stop attacking?"""
		return

	def ai_stop_attacking(self):
		""" npc.ai_stop_attacking() -> none"""
		return

	def anim_goal_interrupt(self):
		""" npc.anim_goal_interrupt() -> none"""
		return

	def begin_dialog(self, target, line):
		"""Schedules a Python dialog time event in 1ms. pc.begin_dialog(PyObjHandle: target, int: line) -> none"""
		return

	def can_sneak_attack(self, target):
		"""npc.can_sneak_attack(PyObjHandle: target) -> int
		Check for:
			self (Sneak Attack Dice) e.g. rogue, otherwise 0
			target DK_QUE_Critter_Is_Immune_Critical_Hits, otherwise 0
			self.CanSense(target), otherwise 0
				self.CanSeeWithBlindsight(target) or
					target.DK_QUE_Critter_Is_Invisible vs self.DK_QUE_Critter_Can_See_Invisible and
					not self.DK_QUE_Critter_Is_Blinded and
					not target.IsConcealed() and
					not target.IsMovingSilently() and 
					not oldCanSense(distance check base hide vs base spot)
		"""
		return

	def critter_flag_set(self, flag):
		"""npc.critter_flag_set(int[OCF_IS_CONCEALED...]: flag) -> None"""
		return

	def critter_flag_unset(self, flag):
		"""npc.critter_flag_unset(int[OCF_IS_CONCEALED...]: flag) -> None"""
		return

	def d20_send_signal(self, signalId, obj):
		"""Send d20 signal. npc.d20_send_signal(int[DK_SIG_HP_Changed+signalId]: signalId, PyObjHandle: obj)"""
		return

	def destroy(self):
		"""Destroys the object"""
		return

	def inventory_item(self, index):
		"""npc.inventory_item(int: index) -> PyObjHandle"""
		return PyObjHandle()

	def item_worn_unwield(self, equip_slot, drop_flag):
		"""Move item to inventory or drop. npc.item_worn_unwield(int[item_wear_helmet-item_wear_lockpicks]: equip_slot, int: drop_flag) -> none"""
		return PyObjHandle()
	
	def feat_add(self, featCode, do_refresh_d20_status):
		"""Adds a feat. npc.feat_add(int[FEAT_ACROBATIC - FEAT_INDOMITABLE_WILL]: featCode, int: do_refresh_d20_status) -> int
		npc.feat_add(string[feat_enums]: featCode) -> int"""
		return 1

	def make_class(self, stat_class, level):
		"""Makes npc to have class levels. npc.make_class(int[stat_level_barbarian - ...]: stat_class, int: level) -> int"""
		return 1

	def make_wiz(self, level):
		"""Makes npc to have wizard levels. npc.make_wiz(int: level) -> int"""
		return 1
	
	def money_get(self):
		"""Get npc money in copper. npc.money_get() -> int"""
		return 1
	
	def money_adj(self, copper):
		"""Add npc coppers, converted to money gp/10 etc. npc.money_adj(int: copper) -> None"""
		return
	
	def npc_flag_set(self, flag):
		"""npc.npc_flag_set(int[ONF_EX_FOLLOWER...]: flag) -> None"""
		return

	def npc_flag_unset(self, flag):
		"""npc.critter_flag_unset(int[ONF_EX_FOLLOWER...]: flag) -> None"""
		return

	def obj_get_int(self, field):
		"""Get internal field int value. npc.obj_get_int(int[obj_f_*]: field) -> int"""
		return 0

	def obj_set_int(self, field, value):
		return


	def pc_add(self, dude):
		""" Adds object as a PC party member.	pc.pc_add(PyObjHandle: dude) -> int"""
		return 0

	def perform_touch_attack(self, target, isMelee):
		""" Performs touch attack (if isMelee=0 then ranged).	pc.perform_touch_attack(PyObjHandle: target, [bool: isMelee]) -> int"""
		return 0

	def portal_toggle_open(self):
		return

	def stat_base_set(self, stat, value):
		"""Sets specific stat. npc.stat_base_set(int[stat_strength-stat_psi_points_cur]: stat, int: value) -> int"""
		return

	def stat_level_get(self, stat, statArg):
		"""get specific stat. npc.stat_level_get(int[stat_strength-stat_psi_points_cur]: stat , int: statArg = None) -> int"""
		return 0


class game(object):
	"""access to game engine"""

	@staticmethod
	def obj_create(protoId, loc):
		""" Will create PyObjHandle based on protoId and place it on location. game.obj_create(int: protoId, int64: loc) -> PyObjHandle"""
		return PyObjHandle()

	@staticmethod
	def make_custom_name(name):
		"""Will create new custom description. game.make_custom_name('new name') -> int: name_id"""
		return 1

	@staticmethod
	def get_feat_name(feat_code):
		""" Get feat name from code. game.get_feat_name(int: feat_code) -> string"""
		return ""
	
	@staticmethod
	def getproto(protoId):
		""" Get proto PyObjHandle based on protoId. game.getproto(int: protoId) -> PyObjHandle"""
		return PyObjHandle()
	

def anyone(targetObjs, methodName, methodArg):
	return PyObjHandle()

class PyObjScripts(object):
	def __getitem__(self, key):
		return PyObjHandle()
	def __setitem__(self, key, value):
		return

RUN_DEFAULT = 1
SKIP_DEFAULT = 0

#obj_f fields
obj_f_3d_render_height = 40
obj_f_aid = 24
obj_f_ammo_begin = 209
obj_f_ammo_end = 218
obj_f_ammo_flags = 210
obj_f_ammo_pad_i64as_1 = 217
obj_f_ammo_pad_i_1 = 213
obj_f_ammo_pad_i_2 = 214
obj_f_ammo_pad_ias_1 = 216
obj_f_ammo_pad_obj_1 = 215
obj_f_ammo_quantity = 211
obj_f_ammo_type = 212
obj_f_animation_handle = 425
obj_f_armor_ac_adj = 221
obj_f_armor_arcane_spell_failure = 223
obj_f_armor_armor_check_penalty = 224
obj_f_armor_begin = 219
obj_f_armor_end = 228
obj_f_armor_flags = 220
obj_f_armor_max_dex_bonus = 222
obj_f_armor_pad_i64as_1 = 227
obj_f_armor_pad_i_1 = 225
obj_f_armor_pad_ias_1 = 226
obj_f_attack_bonus_idx = 76
obj_f_attack_types_idx = 75
obj_f_bag_begin = 272
obj_f_bag_end = 275
obj_f_bag_flags = 273
obj_f_bag_size = 274
obj_f_base_anim = 38
obj_f_base_mesh = 37
obj_f_begin = 0
obj_f_blit_alpha = 11
obj_f_blit_color = 10
obj_f_blit_flags = 9
obj_f_blocking_mask = 21
obj_f_category = 33
obj_f_color = 417
obj_f_colors = 418
obj_f_condition_arg0 = 42
obj_f_conditions = 41
obj_f_container_begin = 102
obj_f_container_end = 120
obj_f_container_flags = 103
obj_f_container_inventory_list_idx = 107
obj_f_container_inventory_num = 106
obj_f_container_inventory_source = 108
obj_f_container_key_id = 105
obj_f_container_lock_dc = 104
obj_f_container_notify_npc = 109
obj_f_container_pad_i64as_1 = 118
obj_f_container_pad_i_1 = 110
obj_f_container_pad_i_2 = 111
obj_f_container_pad_i_3 = 112
obj_f_container_pad_i_4 = 113
obj_f_container_pad_i_5 = 114
obj_f_container_pad_ias_1 = 117
obj_f_container_pad_obj_1 = 115
obj_f_container_pad_obj_2 = 116
obj_f_container_pad_objas_1 = 119
obj_f_critter_abilities_idx = 286
obj_f_critter_age = 290
obj_f_critter_alignment = 295
obj_f_critter_alignment_choice = 299
obj_f_critter_attacks_idx = 332
obj_f_critter_begin = 283
obj_f_critter_damage_idx = 331
obj_f_critter_death_time = 316
obj_f_critter_deity = 296
obj_f_critter_description_unknown = 312
obj_f_critter_domain_1 = 297
obj_f_critter_domain_2 = 298
obj_f_critter_end = 338
obj_f_critter_experience = 293
obj_f_critter_feat_count_idx = 305
obj_f_critter_feat_idx = 304
obj_f_critter_flags = 284
obj_f_critter_flags2 = 285
obj_f_critter_fleeing_from = 306
obj_f_critter_follower_idx = 313
obj_f_critter_gender = 289
obj_f_critter_hair_style = 323
obj_f_critter_height = 291
obj_f_critter_inventory_list_idx = 310
obj_f_critter_inventory_num = 309
obj_f_critter_inventory_source = 311
obj_f_critter_level_idx = 287
obj_f_critter_money_idx = 308
obj_f_critter_monster_category = 326
obj_f_critter_pad_i64_2 = 327
obj_f_critter_pad_i64_3 = 328
obj_f_critter_pad_i64_4 = 329
obj_f_critter_pad_i64_5 = 330
obj_f_critter_pad_i64as_2 = 334
obj_f_critter_pad_i64as_3 = 335
obj_f_critter_pad_i64as_4 = 336
obj_f_critter_pad_i64as_5 = 337
obj_f_critter_pad_i_1 = 294
obj_f_critter_pad_i_3 = 325
obj_f_critter_pad_i_4 = 320
obj_f_critter_pad_i_5 = 321
obj_f_critter_portrait = 307
obj_f_critter_race = 288
obj_f_critter_reach = 318
obj_f_critter_school_specialization = 300
obj_f_critter_seen_maplist = 333
obj_f_critter_sequence = 322
obj_f_critter_skill_idx = 317
obj_f_critter_spells_cast_idx = 303
obj_f_critter_spells_known_idx = 301
obj_f_critter_spells_memorized_idx = 302
obj_f_critter_strategy = 324
obj_f_critter_subdual_damage = 319
obj_f_critter_teleport_dest = 314
obj_f_critter_teleport_map = 315
obj_f_critter_weight = 292
obj_f_current_aid = 1
obj_f_description = 23
obj_f_destroyed_aid = 25
obj_f_dispatcher = 45
obj_f_end = 87
obj_f_find_node = 424
obj_f_flags = 19
obj_f_food_begin = 241
obj_f_food_end = 247
obj_f_food_flags = 242
obj_f_food_pad_i64as_1 = 246
obj_f_food_pad_i_1 = 243
obj_f_food_pad_i_2 = 244
obj_f_food_pad_ias_1 = 245
obj_f_generic_begin = 276
obj_f_generic_end = 282
obj_f_generic_flags = 277
obj_f_generic_pad_i64as_1 = 281
obj_f_generic_pad_ias_1 = 280
obj_f_generic_usage_bonus = 278
obj_f_generic_usage_count_remaining = 279
obj_f_grapple_state = 426
obj_f_hp_adj = 28
obj_f_hp_damage = 29
obj_f_hp_pts = 27
obj_f_initiative = 44
obj_f_internal_flags = 423
obj_f_item_ai_action = 165
obj_f_item_begin = 151
obj_f_item_description_effects = 161
obj_f_item_description_unknown = 160
obj_f_item_end = 186
obj_f_item_flags = 152
obj_f_item_ground_anim = 159
obj_f_item_ground_mesh = 158
obj_f_item_inv_aid = 156
obj_f_item_inv_location = 157
obj_f_item_material_slot = 167
obj_f_item_pad_i64as_1 = 182
obj_f_item_pad_i64as_2 = 183
obj_f_item_pad_i_1 = 169
obj_f_item_pad_i_2 = 170
obj_f_item_pad_i_3 = 171
obj_f_item_pad_i_4 = 172
obj_f_item_pad_i_5 = 173
obj_f_item_pad_i_6 = 174
obj_f_item_pad_obj_1 = 175
obj_f_item_pad_obj_2 = 176
obj_f_item_pad_obj_3 = 177
obj_f_item_pad_obj_4 = 178
obj_f_item_pad_obj_5 = 179
obj_f_item_pad_objas_1 = 184
obj_f_item_pad_objas_2 = 185
obj_f_item_pad_wielder_argument_array = 181
obj_f_item_pad_wielder_condition_array = 180
obj_f_item_parent = 153
obj_f_item_quantity = 168
obj_f_item_spell_charges_idx = 164
obj_f_item_spell_idx = 162
obj_f_item_spell_idx_flags = 163
obj_f_item_wear_flags = 166
obj_f_item_weight = 154
obj_f_item_worth = 155
obj_f_key_begin = 255
obj_f_key_end = 261
obj_f_key_key_id = 256
obj_f_key_pad_i64as_1 = 260
obj_f_key_pad_i_1 = 257
obj_f_key_pad_i_2 = 258
obj_f_key_pad_ias_1 = 259
obj_f_last_hit_by = 69
obj_f_light_aid = 14
obj_f_light_color = 15
obj_f_light_flags = 13
obj_f_light_handle = 421
obj_f_location = 2
obj_f_material = 30
obj_f_money_begin = 229
obj_f_money_end = 240
obj_f_money_flags = 230
obj_f_money_pad_i64as_1 = 239
obj_f_money_pad_i_1 = 233
obj_f_money_pad_i_2 = 234
obj_f_money_pad_i_3 = 235
obj_f_money_pad_i_4 = 236
obj_f_money_pad_i_5 = 237
obj_f_money_pad_ias_1 = 238
obj_f_money_quantity = 231
obj_f_money_type = 232
obj_f_name = 22
obj_f_npc_ac_bonus = 376
obj_f_npc_add_mesh = 377
obj_f_npc_ai_data = 356
obj_f_npc_ai_flags64 = 382
obj_f_npc_ai_list_idx = 372
obj_f_npc_ai_list_type_idx = 388
obj_f_npc_begin = 353
obj_f_npc_challenge_rating = 367
obj_f_npc_combat_focus = 357
obj_f_npc_end = 397
obj_f_npc_faction = 363
obj_f_npc_flags = 354
obj_f_npc_generator_data = 371
obj_f_npc_hitdice_idx = 387
obj_f_npc_leader = 355
obj_f_npc_pad_i64_2 = 383
obj_f_npc_pad_i64_3 = 384
obj_f_npc_pad_i64_4 = 385
obj_f_npc_pad_i64_5 = 386
obj_f_npc_pad_i64as_2 = 393
obj_f_npc_pad_i64as_3 = 394
obj_f_npc_pad_i64as_4 = 395
obj_f_npc_pad_i64as_5 = 396
obj_f_npc_pad_i_3 = 379
obj_f_npc_pad_i_4 = 380
obj_f_npc_pad_i_5 = 381
obj_f_npc_pad_ias_3 = 389
obj_f_npc_pad_ias_4 = 390
obj_f_npc_pad_ias_5 = 391
obj_f_npc_reaction_base = 366
obj_f_npc_reaction_level_idx = 369
obj_f_npc_reaction_pc_idx = 368
obj_f_npc_reaction_time_idx = 370
obj_f_npc_retail_price_multiplier = 364
obj_f_npc_save_fortitude_bonus = 374
obj_f_npc_save_reflexes_bonus = 373
obj_f_npc_save_willpower_bonus = 375
obj_f_npc_standpoint_day_INTERNAL_DO_NOT_USE = 361
obj_f_npc_standpoint_night_INTERNAL_DO_NOT_USE = 362
obj_f_npc_standpoints = 392
obj_f_npc_substitute_inventory = 365
obj_f_npc_waypoint_anim = 378
obj_f_npc_waypoint_current = 360
obj_f_npc_waypoints_idx = 359
obj_f_npc_who_hit_me_last = 358
obj_f_offset_x = 3
obj_f_offset_y = 4
obj_f_offset_z = 54
obj_f_overlay_back = 7
obj_f_overlay_fore = 6
obj_f_overlay_light_aid = 17
obj_f_overlay_light_color = 18
obj_f_overlay_light_flags = 16
obj_f_overlay_light_handles = 422
obj_f_pad_f_0 = 63
obj_f_pad_f_3 = 56
obj_f_pad_f_4 = 57
obj_f_pad_f_5 = 58
obj_f_pad_f_6 = 59
obj_f_pad_f_7 = 60
obj_f_pad_f_8 = 61
obj_f_pad_f_9 = 62
obj_f_pad_i64_0 = 64
obj_f_pad_i64_1 = 65
obj_f_pad_i64_2 = 66
obj_f_pad_i64_3 = 67
obj_f_pad_i64_4 = 68
obj_f_pad_i64as_0 = 79
obj_f_pad_i64as_1 = 80
obj_f_pad_i64as_2 = 81
obj_f_pad_i64as_3 = 82
obj_f_pad_i64as_4 = 83
obj_f_pad_i_0 = 53
obj_f_pad_i_7 = 50
obj_f_pad_i_8 = 51
obj_f_pad_i_9 = 52
obj_f_pad_ias_4 = 78
obj_f_pad_obj_1 = 70
obj_f_pad_obj_2 = 71
obj_f_pad_obj_3 = 72
obj_f_pad_obj_4 = 73
obj_f_pad_objas_0 = 84
obj_f_pad_objas_1 = 85
obj_f_pad_objas_2 = 86
obj_f_palette = 416
obj_f_pc_begin = 339
obj_f_pc_end = 352
obj_f_pc_flags = 340
obj_f_pc_global_flags = 344
obj_f_pc_global_variables = 345
obj_f_pc_pad_i64as_0 = 342
obj_f_pc_pad_i64as_1 = 351
obj_f_pc_pad_i_2 = 348
obj_f_pc_pad_ias_0 = 341
obj_f_pc_pad_ias_2 = 350
obj_f_pc_player_name = 343
obj_f_pc_roll_count = 347
obj_f_pc_voice_idx = 346
obj_f_pc_weaponslots_idx = 349
obj_f_permanent_mod_data = 74
obj_f_permanent_mods = 43
obj_f_portal_begin = 88
obj_f_portal_end = 101
obj_f_portal_flags = 89
obj_f_portal_key_id = 91
obj_f_portal_lock_dc = 90
obj_f_portal_notify_npc = 92
obj_f_portal_pad_i64as_1 = 100
obj_f_portal_pad_i_1 = 93
obj_f_portal_pad_i_2 = 94
obj_f_portal_pad_i_3 = 95
obj_f_portal_pad_i_4 = 96
obj_f_portal_pad_i_5 = 97
obj_f_portal_pad_ias_1 = 99
obj_f_portal_pad_obj_1 = 98
obj_f_projectile_acceleration_x = 140
obj_f_projectile_acceleration_y = 141
obj_f_projectile_acceleration_z = 142
obj_f_projectile_begin = 134
obj_f_projectile_end = 150
obj_f_projectile_flags_combat = 135
obj_f_projectile_flags_combat_damage = 136
obj_f_projectile_pad_i64as_1 = 148
obj_f_projectile_pad_i_4 = 143
obj_f_projectile_pad_ias_1 = 147
obj_f_projectile_pad_obj_1 = 144
obj_f_projectile_pad_obj_2 = 145
obj_f_projectile_pad_obj_3 = 146
obj_f_projectile_pad_objas_1 = 149
obj_f_projectile_parent_ammo = 138
obj_f_projectile_parent_weapon = 137
obj_f_projectile_part_sys_id = 139
obj_f_prototype_handle = 429
obj_f_radius = 39
obj_f_render_alpha = 411
obj_f_render_color = 407
obj_f_render_colors = 408
obj_f_render_flags = 419
obj_f_render_height = 415
obj_f_render_palette = 409
obj_f_render_scale = 410
obj_f_render_width = 414
obj_f_render_x = 412
obj_f_render_y = 413
obj_f_rotation = 34
obj_f_rotation_pitch = 55
obj_f_scale = 12
obj_f_scenery_begin = 121
obj_f_scenery_end = 133
obj_f_scenery_flags = 122
obj_f_scenery_pad_i64as_1 = 132
obj_f_scenery_pad_i_0 = 125
obj_f_scenery_pad_i_1 = 126
obj_f_scenery_pad_i_4 = 128
obj_f_scenery_pad_i_5 = 129
obj_f_scenery_pad_ias_1 = 131
obj_f_scenery_pad_obj_0 = 123
obj_f_scenery_pad_obj_1 = 130
obj_f_scenery_respawn_delay = 124
obj_f_scenery_teleport_to = 127
obj_f_scripts_idx = 31
obj_f_scroll_begin = 248
obj_f_scroll_end = 254
obj_f_scroll_flags = 249
obj_f_scroll_pad_i64as_1 = 253
obj_f_scroll_pad_i_1 = 250
obj_f_scroll_pad_i_2 = 251
obj_f_scroll_pad_ias_1 = 252
obj_f_secretdoor_dc = 49
obj_f_secretdoor_effectname = 48
obj_f_secretdoor_flags = 47
obj_f_shadow = 5
obj_f_size = 26
obj_f_sound_effect = 32
obj_f_speed_run = 36
obj_f_speed_walk = 35
obj_f_spell_flags = 20
obj_f_strategy_state = 77
obj_f_subinitiative = 46
obj_f_temp_id = 420
obj_f_total_normal = 405
obj_f_transient_begin = 406
obj_f_transient_end = 427
obj_f_trap_begin = 398
obj_f_trap_difficulty = 400
obj_f_trap_end = 404
obj_f_trap_flags = 399
obj_f_trap_pad_i64as_1 = 403
obj_f_trap_pad_i_2 = 401
obj_f_trap_pad_ias_1 = 402
obj_f_type = 428
obj_f_underlay = 8
obj_f_weapon_ammo_consumption = 191
obj_f_weapon_ammo_type = 190
obj_f_weapon_animtype = 196
obj_f_weapon_attacktype = 194
obj_f_weapon_begin = 187
obj_f_weapon_crit_hit_chart = 193
obj_f_weapon_crit_range = 198
obj_f_weapon_damage_dice = 195
obj_f_weapon_end = 208
obj_f_weapon_flags = 188
obj_f_weapon_missile_aid = 192
obj_f_weapon_pad_i64as_1 = 207
obj_f_weapon_pad_i_1 = 199
obj_f_weapon_pad_i_2 = 200
obj_f_weapon_pad_ias_1 = 206
obj_f_weapon_pad_obj_1 = 201
obj_f_weapon_pad_obj_2 = 202
obj_f_weapon_pad_obj_3 = 203
obj_f_weapon_pad_obj_4 = 204
obj_f_weapon_pad_obj_5 = 205
obj_f_weapon_range = 189
obj_f_weapon_type = 197
obj_f_written_begin = 262
obj_f_written_end = 271
obj_f_written_flags = 263
obj_f_written_pad_i64as_1 = 270
obj_f_written_pad_i_1 = 267
obj_f_written_pad_i_2 = 268
obj_f_written_pad_ias_1 = 269
obj_f_written_subtype = 264
obj_f_written_text_end_line = 266
obj_f_written_text_start_line = 265


# obj_f types
obj_t_ammo = 5
obj_t_armor = 6
obj_t_bag = 16
obj_t_container = 1
obj_t_food = 8
obj_t_generic = 12
obj_t_key = 10
obj_t_money = 7
obj_t_npc = 14
obj_t_pc = 13
obj_t_portal = 0
obj_t_projectile = 3
obj_t_scenery = 2
obj_t_scroll = 9
obj_t_trap = 15
obj_t_weapon = 4
obj_t_written = 11

item_wear_ammo = 9
item_wear_armor = 5
item_wear_bardic_item = 14
item_wear_boots = 8
item_wear_bracers = 13
item_wear_cloak = 10
item_wear_gloves = 2
item_wear_helmet = 0
item_wear_lockpicks = 15
item_wear_necklace = 1
item_wear_ring_primary = 6
item_wear_ring_secondary = 7
item_wear_robes = 12
item_wear_shield = 11
item_wear_weapon_primary = 3
item_wear_weapon_secondary = 4

feat_abundant_step = 659
feat_acrobatic = 0
feat_agile = 1
feat_alertness = 2
feat_ambidexterity_ranger = 639
feat_animal_affinity = 3
feat_animal_companion = 642
feat_armor_proficiency_druid = 597
feat_armor_proficiency_heavy = 6
feat_armor_proficiency_light = 4
feat_armor_proficiency_medium = 5
feat_associates = 573
feat_athletic = 7
feat_augment_summoning = 8
feat_aura_of_courage = 568
feat_barbarian_rage = 561
feat_bardic_knowledge = 590
feat_bardic_music = 589
feat_blind_fight = 9
feat_brew_potion = 10
feat_call_familiar = 610
feat_cleave = 11
feat_code_of_conduct = 572
feat_combat_casting = 12
feat_combat_expertise = 13
feat_combat_reflexes = 580
feat_craft_magic_arms_and_armor = 14
feat_craft_rod = 15
feat_craft_staff = 16
feat_craft_wand = 17
feat_craft_wondrous_item = 18
feat_crippling_strike = 606
feat_deadly_precision = 672
feat_deceitful = 19
feat_defensive_roll = 574
feat_deflect_arrows = 23
feat_deft_hands = 20
feat_detect_evil = 567
feat_diamond_body = 658
feat_diamond_soul = 660
feat_diehard = 21
feat_diligent = 22
feat_divine_grace = 570
feat_divine_health = 569
feat_divine_might = 668
feat_dodge = 24
feat_domain_power = 577
feat_empower_spell = 25
feat_empty_body = 662
feat_endurance = 26
feat_enlarge_spell = 27
feat_eschew_materials = 28
feat_evasion = 599
feat_exotic_weapon_proficiency_bastard_sword = 36
feat_exotic_weapon_proficiency_dire_flail = 41
feat_exotic_weapon_proficiency_dwarven_urgrosh = 43
feat_exotic_weapon_proficiency_dwarven_waraxe = 37
feat_exotic_weapon_proficiency_gnome_hooked_hammer = 38
feat_exotic_weapon_proficiency_halfling_kama = 29
feat_exotic_weapon_proficiency_halfling_nunchaku = 31
feat_exotic_weapon_proficiency_halfling_siangham = 32
feat_exotic_weapon_proficiency_hand_crossbow = 44
feat_exotic_weapon_proficiency_head = 650
feat_exotic_weapon_proficiency_kama = 33
feat_exotic_weapon_proficiency_kukri = 30
feat_exotic_weapon_proficiency_net = 48
feat_exotic_weapon_proficiency_nunchaku = 34
feat_exotic_weapon_proficiency_orc_double_axe = 39
feat_exotic_weapon_proficiency_repeating_crossbow = 47
feat_exotic_weapon_proficiency_shuriken = 45
feat_exotic_weapon_proficiency_siangham = 35
feat_exotic_weapon_proficiency_spike_chain = 40
feat_exotic_weapon_proficiency_two_bladed_sword = 42
feat_exotic_weapon_proficiency_whip = 46
feat_extend_spell = 49
feat_extra_turning = 50
feat_far_shot = 51
feat_fast_movement = 588
feat_favored_enemy_aberration = 611
feat_favored_enemy_animal = 612
feat_favored_enemy_beast = 613
feat_favored_enemy_construct = 614
feat_favored_enemy_dragon = 615
feat_favored_enemy_elemental = 616
feat_favored_enemy_fey = 617
feat_favored_enemy_giant = 618
feat_favored_enemy_humanoid_dwarf = 632
feat_favored_enemy_humanoid_elf = 633
feat_favored_enemy_humanoid_gnoll = 634
feat_favored_enemy_humanoid_gnome = 635
feat_favored_enemy_humanoid_goblinoid = 630
feat_favored_enemy_humanoid_halfling = 636
feat_favored_enemy_humanoid_human = 638
feat_favored_enemy_humanoid_orc = 637
feat_favored_enemy_humanoid_reptilian = 631
feat_favored_enemy_magical_beast = 619
feat_favored_enemy_monstrous_humanoid = 620
feat_favored_enemy_ooze = 621
feat_favored_enemy_outsider_chaotic = 629
feat_favored_enemy_outsider_evil = 626
feat_favored_enemy_outsider_good = 627
feat_favored_enemy_outsider_lawful = 628
feat_favored_enemy_plant = 622
feat_favored_enemy_shapechanger = 623
feat_favored_enemy_undead = 624
feat_favored_enemy_vermin = 625
feat_flurry_of_blows = 598
feat_forge_ring = 52
feat_great_cleave = 53
feat_great_fortitude = 54
feat_greater_rage = 675
feat_greater_spell_focus_abjuration = 55
feat_greater_spell_focus_conjuration = 56
feat_greater_spell_focus_divination = 57
feat_greater_spell_focus_enchantment = 58
feat_greater_spell_focus_evocation = 59
feat_greater_spell_focus_illusion = 60
feat_greater_spell_focus_necromancy = 61
feat_greater_spell_focus_transmutation = 62
feat_greater_spell_penetration = 63
feat_greater_two_weapon_fighting = 64
feat_greater_two_weapon_fighting_ranger = 664
feat_greater_weapon_focus_bastard_sword = 122
feat_greater_weapon_focus_battleaxe = 91
feat_greater_weapon_focus_club = 73
feat_greater_weapon_focus_composite_longbow = 114
feat_greater_weapon_focus_composite_shortbow = 112
feat_greater_weapon_focus_dagger = 68
feat_greater_weapon_focus_dart = 80
feat_greater_weapon_focus_dire_flail = 127
feat_greater_weapon_focus_dwarven_urgrosh = 129
feat_greater_weapon_focus_dwarven_waraxe = 123
feat_greater_weapon_focus_falchion = 100
feat_greater_weapon_focus_gauntlet = 65
feat_greater_weapon_focus_glaive = 102
feat_greater_weapon_focus_gnome_hooked_hammer = 124
feat_greater_weapon_focus_grapple = 135
feat_greater_weapon_focus_greataxe = 103
feat_greater_weapon_focus_greatclub = 104
feat_greater_weapon_focus_greatsword = 105
feat_greater_weapon_focus_guisarme = 106
feat_greater_weapon_focus_halberd = 107
feat_greater_weapon_focus_halfling_kama = 115
feat_greater_weapon_focus_halfling_nunchaku = 117
feat_greater_weapon_focus_halfling_siangham = 118
feat_greater_weapon_focus_halfspear = 74
feat_greater_weapon_focus_hand_crossbow = 130
feat_greater_weapon_focus_handaxe = 86
feat_greater_weapon_focus_head = 656
feat_greater_weapon_focus_heavy_crossbow = 82
feat_greater_weapon_focus_heavy_flail = 101
feat_greater_weapon_focus_heavy_lance = 93
feat_greater_weapon_focus_heavy_mace = 75
feat_greater_weapon_focus_heavy_pick = 95
feat_greater_weapon_focus_javelin = 83
feat_greater_weapon_focus_kama = 119
feat_greater_weapon_focus_kukri = 116
feat_greater_weapon_focus_light_crossbow = 79
feat_greater_weapon_focus_light_flail = 92
feat_greater_weapon_focus_light_hammer = 85
feat_greater_weapon_focus_light_lance = 87
feat_greater_weapon_focus_light_mace = 71
feat_greater_weapon_focus_light_pick = 88
feat_greater_weapon_focus_longbow = 113
feat_greater_weapon_focus_longspear = 108
feat_greater_weapon_focus_longsword = 94
feat_greater_weapon_focus_morningstar = 76
feat_greater_weapon_focus_net = 134
feat_greater_weapon_focus_nunchaku = 120
feat_greater_weapon_focus_orc_double_axe = 125
feat_greater_weapon_focus_punching_dagger = 69
feat_greater_weapon_focus_quarterstaff = 77
feat_greater_weapon_focus_ranseur = 109
feat_greater_weapon_focus_rapier = 96
feat_greater_weapon_focus_ray = 136
feat_greater_weapon_focus_repeating_crossbow = 133
feat_greater_weapon_focus_sap = 89
feat_greater_weapon_focus_scimitar = 97
feat_greater_weapon_focus_scythe = 110
feat_greater_weapon_focus_short_sword = 90
feat_greater_weapon_focus_shortbow = 111
feat_greater_weapon_focus_shortspear = 78
feat_greater_weapon_focus_shuriken = 131
feat_greater_weapon_focus_siangham = 121
feat_greater_weapon_focus_sickle = 72
feat_greater_weapon_focus_sling = 81
feat_greater_weapon_focus_spike_chain = 126
feat_greater_weapon_focus_spiked_gauntlet = 70
feat_greater_weapon_focus_throwing_axe = 84
feat_greater_weapon_focus_trident = 98
feat_greater_weapon_focus_two_bladed_sword = 128
feat_greater_weapon_focus_unarmed_strike_medium_sized_being = 66
feat_greater_weapon_focus_unarmed_strike_small_being = 67
feat_greater_weapon_focus_warhammer = 99
feat_greater_weapon_focus_whip = 132
feat_greater_weapon_specialization = 137
feat_greater_weapon_specialization_bastard_sword = 733
feat_greater_weapon_specialization_battleaxe = 702
feat_greater_weapon_specialization_butterfly_sword = 726
feat_greater_weapon_specialization_club = 684
feat_greater_weapon_specialization_composite_longbow = 725
feat_greater_weapon_specialization_composite_shortbow = 723
feat_greater_weapon_specialization_dagger = 679
feat_greater_weapon_specialization_dart = 691
feat_greater_weapon_specialization_dire_flail = 738
feat_greater_weapon_specialization_dwarven_urgrosh = 740
feat_greater_weapon_specialization_dwarven_waraxe = 734
feat_greater_weapon_specialization_falchion = 711
feat_greater_weapon_specialization_gauntlet = 676
feat_greater_weapon_specialization_glaive = 713
feat_greater_weapon_specialization_gnome_hooked_hammer = 735
feat_greater_weapon_specialization_grapple = 746
feat_greater_weapon_specialization_greataxe = 714
feat_greater_weapon_specialization_greatclub = 715
feat_greater_weapon_specialization_greatsword = 716
feat_greater_weapon_specialization_guisarme = 717
feat_greater_weapon_specialization_halberd = 718
feat_greater_weapon_specialization_hand_crossbow = 741
feat_greater_weapon_specialization_handaxe = 697
feat_greater_weapon_specialization_heavy_crossbow = 693
feat_greater_weapon_specialization_heavy_flail = 712
feat_greater_weapon_specialization_heavy_lance = 704
feat_greater_weapon_specialization_heavy_mace = 686
feat_greater_weapon_specialization_heavy_pick = 706
feat_greater_weapon_specialization_javelin = 694
feat_greater_weapon_specialization_kama = 730
feat_greater_weapon_specialization_kukri = 727
feat_greater_weapon_specialization_light_crossbow = 690
feat_greater_weapon_specialization_light_flail = 703
feat_greater_weapon_specialization_light_hammer = 696
feat_greater_weapon_specialization_light_lance = 698
feat_greater_weapon_specialization_light_mace = 682
feat_greater_weapon_specialization_light_pick = 699
feat_greater_weapon_specialization_longbow = 724
feat_greater_weapon_specialization_longspear = 719
feat_greater_weapon_specialization_longsword = 705
feat_greater_weapon_specialization_monk_spade = 729
feat_greater_weapon_specialization_morningstar = 687
feat_greater_weapon_specialization_net = 745
feat_greater_weapon_specialization_orc_double_axe = 736
feat_greater_weapon_specialization_punching_dagger = 680
feat_greater_weapon_specialization_quarterstaff = 688
feat_greater_weapon_specialization_ranseur = 720
feat_greater_weapon_specialization_rapier = 707
feat_greater_weapon_specialization_repeating_crossbow = 744
feat_greater_weapon_specialization_sap = 700
feat_greater_weapon_specialization_scimitar = 708
feat_greater_weapon_specialization_scythe = 721
feat_greater_weapon_specialization_short_sword = 701
feat_greater_weapon_specialization_shortbow = 722
feat_greater_weapon_specialization_shortspear = 685
feat_greater_weapon_specialization_shuriken = 742
feat_greater_weapon_specialization_siangham = 732
feat_greater_weapon_specialization_sickle = 683
feat_greater_weapon_specialization_sling = 692
feat_greater_weapon_specialization_spear = 689
feat_greater_weapon_specialization_spike_chain = 737
feat_greater_weapon_specialization_spiked_gauntlet = 681
feat_greater_weapon_specialization_throwing_axe = 695
feat_greater_weapon_specialization_tonfa = 731
feat_greater_weapon_specialization_trident = 709
feat_greater_weapon_specialization_two_bladed_sword = 739
feat_greater_weapon_specialization_unarmed_strike = 677
feat_greater_weapon_specialization_unarmed_strike_small_being = 678
feat_greater_weapon_specialization_war_fan = 728
feat_greater_weapon_specialization_warhammer = 710
feat_greater_weapon_specialization_whip = 743
feat_heighten_spell = 138
feat_improved_bull_rush = 139
feat_improved_counterspell = 140
feat_improved_critical_bastard_sword = 198
feat_improved_critical_battleaxe = 167
feat_improved_critical_club = 149
feat_improved_critical_composite_longbow = 190
feat_improved_critical_composite_shortbow = 188
feat_improved_critical_dagger = 144
feat_improved_critical_dart = 156
feat_improved_critical_dire_flail = 203
feat_improved_critical_dwarven_urgrosh = 205
feat_improved_critical_dwarven_waraxe = 199
feat_improved_critical_falchion = 176
feat_improved_critical_gauntlet = 141
feat_improved_critical_glaive = 178
feat_improved_critical_gnome_hooked_hammer = 200
feat_improved_critical_greataxe = 179
feat_improved_critical_greatclub = 180
feat_improved_critical_greatsword = 181
feat_improved_critical_guisarme = 182
feat_improved_critical_halberd = 183
feat_improved_critical_halfling_kama = 191
feat_improved_critical_halfling_nunchaku = 193
feat_improved_critical_halfling_siangham = 194
feat_improved_critical_halfspear = 150
feat_improved_critical_hand_crossbow = 206
feat_improved_critical_handaxe = 162
feat_improved_critical_head = 651
feat_improved_critical_heavy_crossbow = 158
feat_improved_critical_heavy_flail = 177
feat_improved_critical_heavy_lance = 169
feat_improved_critical_heavy_mace = 151
feat_improved_critical_heavy_pick = 171
feat_improved_critical_javelin = 159
feat_improved_critical_kama = 195
feat_improved_critical_kukri = 192
feat_improved_critical_light_crossbow = 155
feat_improved_critical_light_flail = 168
feat_improved_critical_light_hammer = 161
feat_improved_critical_light_lance = 163
feat_improved_critical_light_mace = 147
feat_improved_critical_light_pick = 164
feat_improved_critical_longbow = 189
feat_improved_critical_longspear = 184
feat_improved_critical_longsword = 170
feat_improved_critical_morningstar = 152
feat_improved_critical_net = 210
feat_improved_critical_nunchaku = 196
feat_improved_critical_orc_double_axe = 201
feat_improved_critical_punching_dagger = 145
feat_improved_critical_quarterstaff = 153
feat_improved_critical_ranseur = 185
feat_improved_critical_rapier = 172
feat_improved_critical_repeating_crossbow = 209
feat_improved_critical_sap = 165
feat_improved_critical_scimitar = 173
feat_improved_critical_scythe = 186
feat_improved_critical_short_sword = 166
feat_improved_critical_shortbow = 187
feat_improved_critical_shortspear = 154
feat_improved_critical_shuriken = 207
feat_improved_critical_siangham = 197
feat_improved_critical_sickle = 148
feat_improved_critical_sling = 157
feat_improved_critical_spike_chain = 202
feat_improved_critical_spiked_gauntlet = 146
feat_improved_critical_throwing_axe = 160
feat_improved_critical_trident = 174
feat_improved_critical_two_bladed_sword = 204
feat_improved_critical_unarmed_strike_medium_sized_being = 142
feat_improved_critical_unarmed_strike_small_being = 143
feat_improved_critical_warhammer = 175
feat_improved_critical_whip = 208
feat_improved_disarm = 211
feat_improved_evasion = 602
feat_improved_feint = 212
feat_improved_grapple = 213
feat_improved_initiative = 214
feat_improved_overrun = 215
feat_improved_precise_shot = 665
feat_improved_precise_shot_ranger = 666
feat_improved_shield_bash = 216
feat_improved_trip = 217
feat_improved_turning = 219
feat_improved_two_weapon_fighting = 218
feat_improved_two_weapon_fighting_ranger = 641
feat_improved_unarmed_strike = 220
feat_improved_uncanny_dodge = 221
feat_indomitable_will = 749
feat_investigator = 222
feat_iron_will = 223
feat_ki_strike = 603
feat_knock_down = 670
feat_lay_on_hands = 564
feat_leadership = 224
feat_lightning_reflexes = 225
feat_magical_affinity = 226
feat_manyshot = 227
feat_martial_weapon_proficiency_all = 581
feat_martial_weapon_proficiency_battleaxe = 235
feat_martial_weapon_proficiency_composite_longbow = 258
feat_martial_weapon_proficiency_composite_shortbow = 256
feat_martial_weapon_proficiency_falchion = 244
feat_martial_weapon_proficiency_glaive = 246
feat_martial_weapon_proficiency_greataxe = 247
feat_martial_weapon_proficiency_greatclub = 248
feat_martial_weapon_proficiency_greatsword = 249
feat_martial_weapon_proficiency_guisarme = 250
feat_martial_weapon_proficiency_halberd = 251
feat_martial_weapon_proficiency_handaxe = 230
feat_martial_weapon_proficiency_head = 652
feat_martial_weapon_proficiency_heavy_flail = 245
feat_martial_weapon_proficiency_heavy_lance = 237
feat_martial_weapon_proficiency_heavy_pick = 239
feat_martial_weapon_proficiency_light_flail = 236
feat_martial_weapon_proficiency_light_hammer = 229
feat_martial_weapon_proficiency_light_lance = 231
feat_martial_weapon_proficiency_light_pick = 232
feat_martial_weapon_proficiency_longbow = 257
feat_martial_weapon_proficiency_longspear = 252
feat_martial_weapon_proficiency_longsword = 238
feat_martial_weapon_proficiency_ranseur = 253
feat_martial_weapon_proficiency_rapier = 240
feat_martial_weapon_proficiency_sap = 233
feat_martial_weapon_proficiency_scimitar = 241
feat_martial_weapon_proficiency_scythe = 254
feat_martial_weapon_proficiency_short_sword = 234
feat_martial_weapon_proficiency_shortbow = 255
feat_martial_weapon_proficiency_throwing_axe = 228
feat_martial_weapon_proficiency_trident = 242
feat_martial_weapon_proficiency_warhammer = 243
feat_maximize_spell = 259
feat_mighty_rage = 748
feat_mobility = 260
feat_mounted_archery = 261
feat_mounted_combat = 262
feat_natural_spell = 263
feat_nature_sense = 591
feat_negotiator = 264
feat_nimble_fingers = 265
feat_none = 649
feat_opportunist = 607
feat_perfect_self = 663
feat_persistent_spell = 673
feat_persuasive = 266
feat_point_blank_shot = 267
feat_power_attack = 268
feat_power_critical = 674
feat_precise_shot = 269
feat_purity_of_body = 601
feat_quick_draw = 270
feat_quicken_spell = 271
feat_quivering_palm = 661
feat_ranger_archery_style = 644
feat_ranger_manyshot = 647
feat_ranger_rapid_shot = 646
feat_ranger_two_weapon_style = 643
feat_rapid_reload = 273
feat_rapid_shot = 272
feat_rebuke_undead = 576
feat_reckless_offense = 669
feat_remove_disease = 566
feat_resist_natures_lure = 594
feat_ride_by_attack = 274
feat_run = 275
feat_scribe_scroll = 276
feat_self_sufficient = 277
feat_sharp_shooting = 667
feat_shield_proficiency = 278
feat_shot_on_the_run = 279
feat_silent_spell = 280
feat_simple_weapon_proficiency = 281
feat_simple_weapon_proficiency_bard = 648
feat_simple_weapon_proficiency_druid = 582
feat_simple_weapon_proficiency_elf = 586
feat_simple_weapon_proficiency_monk = 583
feat_simple_weapon_proficiency_rogue = 584
feat_simple_weapon_proficiency_wizard = 585
feat_skill_focus_alchemy = 282
feat_skill_focus_animal_empathy = 283
feat_skill_focus_appraise = 284
feat_skill_focus_balance = 285
feat_skill_focus_bluff = 286
feat_skill_focus_climb = 287
feat_skill_focus_concentration = 288
feat_skill_focus_craft = 289
feat_skill_focus_decipher_script = 290
feat_skill_focus_diplomacy = 291
feat_skill_focus_disable_device = 292
feat_skill_focus_disguise = 293
feat_skill_focus_escape_artist = 294
feat_skill_focus_forgery = 295
feat_skill_focus_gather_information = 296
feat_skill_focus_handle_animal = 297
feat_skill_focus_head = 653
feat_skill_focus_heal = 298
feat_skill_focus_hide = 299
feat_skill_focus_innuendo = 300
feat_skill_focus_intimidate = 301
feat_skill_focus_intuit_direction = 302
feat_skill_focus_jump = 303
feat_skill_focus_knowledge = 304
feat_skill_focus_listen = 305
feat_skill_focus_move_silently = 306
feat_skill_focus_open_lock = 307
feat_skill_focus_performance = 308
feat_skill_focus_profession = 310
feat_skill_focus_read_lips = 311
feat_skill_focus_ride = 312
feat_skill_focus_scry = 313
feat_skill_focus_search = 314
feat_skill_focus_sense_motive = 315
feat_skill_focus_slight_of_hand = 309
feat_skill_focus_speak_language = 316
feat_skill_focus_spellcraft = 317
feat_skill_focus_spot = 318
feat_skill_focus_survival = 323
feat_skill_focus_swim = 319
feat_skill_focus_tumble = 320
feat_skill_focus_use_magic_device = 321
feat_skill_focus_use_rope = 322
feat_skill_mastery = 608
feat_slippery_mind = 609
feat_smite_evil = 565
feat_snatch_arrows = 324
feat_sneak_attack = 604
feat_special_mount = 571
feat_spell_focus_abjuration = 325
feat_spell_focus_conjuration = 326
feat_spell_focus_divination = 327
feat_spell_focus_enchantment = 328
feat_spell_focus_evocation = 329
feat_spell_focus_illusion = 330
feat_spell_focus_necromancy = 331
feat_spell_focus_transmutation = 332
feat_spell_mastery = 333
feat_spell_penetration = 334
feat_spirited_charge = 335
feat_spontaneous_casting_cure = 578
feat_spontaneous_casting_inflict = 579
feat_spring_attack = 336
feat_stealthy = 337
feat_still_mind = 600
feat_still_spell = 338
feat_stunning_attacks = 562
feat_stunning_fist = 339
feat_sunder = 340
feat_superior_expertise = 671
feat_tireless_rage = 747
feat_toughness = 341
feat_tower_shield_proficiency = 342
feat_track = 343
feat_trackless_step = 593
feat_trample = 344
feat_traps = 605
feat_turn_undead = 575
feat_two_weapon_defense = 346
feat_two_weapon_fighting = 345
feat_two_weapon_fighting_ranger = 640
feat_uncanny_dodge = 587
feat_venom_immunity = 596
feat_weapon_finesse_bastard_sword = 404
feat_weapon_finesse_battleaxe = 373
feat_weapon_finesse_club = 355
feat_weapon_finesse_composite_longbow = 396
feat_weapon_finesse_composite_shortbow = 394
feat_weapon_finesse_dagger = 350
feat_weapon_finesse_dart = 362
feat_weapon_finesse_dire_flail = 409
feat_weapon_finesse_dwarven_urgrosh = 411
feat_weapon_finesse_dwarven_waraxe = 405
feat_weapon_finesse_falchion = 382
feat_weapon_finesse_gauntlet = 347
feat_weapon_finesse_glaive = 384
feat_weapon_finesse_gnome_hooked_hammer = 406
feat_weapon_finesse_greataxe = 385
feat_weapon_finesse_greatclub = 386
feat_weapon_finesse_greatsword = 387
feat_weapon_finesse_guisarme = 388
feat_weapon_finesse_halberd = 389
feat_weapon_finesse_halfling_kama = 397
feat_weapon_finesse_halfling_nunchaku = 399
feat_weapon_finesse_halfling_siangham = 400
feat_weapon_finesse_halfspear = 356
feat_weapon_finesse_hand_crossbow = 412
feat_weapon_finesse_handaxe = 368
feat_weapon_finesse_head = 654
feat_weapon_finesse_heavy_crossbow = 364
feat_weapon_finesse_heavy_flail = 383
feat_weapon_finesse_heavy_lance = 375
feat_weapon_finesse_heavy_mace = 357
feat_weapon_finesse_heavy_pick = 377
feat_weapon_finesse_javelin = 365
feat_weapon_finesse_kama = 401
feat_weapon_finesse_kukri = 398
feat_weapon_finesse_light_crossbow = 361
feat_weapon_finesse_light_flail = 374
feat_weapon_finesse_light_hammer = 367
feat_weapon_finesse_light_lance = 369
feat_weapon_finesse_light_mace = 353
feat_weapon_finesse_light_pick = 370
feat_weapon_finesse_longbow = 395
feat_weapon_finesse_longspear = 390
feat_weapon_finesse_longsword = 376
feat_weapon_finesse_morningstar = 358
feat_weapon_finesse_net = 416
feat_weapon_finesse_nunchaku = 402
feat_weapon_finesse_orc_double_axe = 407
feat_weapon_finesse_punching_dagger = 351
feat_weapon_finesse_quarterstaff = 359
feat_weapon_finesse_ranseur = 391
feat_weapon_finesse_rapier = 378
feat_weapon_finesse_repeating_crossbow = 415
feat_weapon_finesse_sap = 371
feat_weapon_finesse_scimitar = 379
feat_weapon_finesse_scythe = 392
feat_weapon_finesse_short_sword = 372
feat_weapon_finesse_shortbow = 393
feat_weapon_finesse_shortspear = 360
feat_weapon_finesse_shuriken = 413
feat_weapon_finesse_siangham = 403
feat_weapon_finesse_sickle = 354
feat_weapon_finesse_sling = 363
feat_weapon_finesse_spike_chain = 408
feat_weapon_finesse_spiked_gauntlet = 352
feat_weapon_finesse_throwing_axe = 366
feat_weapon_finesse_trident = 380
feat_weapon_finesse_two_bladed_sword = 410
feat_weapon_finesse_unarmed_strike_medium_sized_being = 348
feat_weapon_finesse_unarmed_strike_small_being = 349
feat_weapon_finesse_warhammer = 381
feat_weapon_finesse_whip = 414
feat_weapon_focus_bastard_sword = 474
feat_weapon_focus_battleaxe = 443
feat_weapon_focus_club = 425
feat_weapon_focus_composite_longbow = 466
feat_weapon_focus_composite_shortbow = 464
feat_weapon_focus_dagger = 420
feat_weapon_focus_dart = 432
feat_weapon_focus_dire_flail = 479
feat_weapon_focus_dwarven_urgrosh = 481
feat_weapon_focus_dwarven_waraxe = 475
feat_weapon_focus_falchion = 452
feat_weapon_focus_gauntlet = 417
feat_weapon_focus_glaive = 454
feat_weapon_focus_gnome_hooked_hammer = 476
feat_weapon_focus_grapple = 487
feat_weapon_focus_greataxe = 455
feat_weapon_focus_greatclub = 456
feat_weapon_focus_greatsword = 457
feat_weapon_focus_guisarme = 458
feat_weapon_focus_halberd = 459
feat_weapon_focus_halfling_kama = 467
feat_weapon_focus_halfling_nunchaku = 469
feat_weapon_focus_halfling_siangham = 470
feat_weapon_focus_halfspear = 426
feat_weapon_focus_hand_crossbow = 482
feat_weapon_focus_handaxe = 438
feat_weapon_focus_head = 655
feat_weapon_focus_heavy_crossbow = 434
feat_weapon_focus_heavy_flail = 453
feat_weapon_focus_heavy_lance = 445
feat_weapon_focus_heavy_mace = 427
feat_weapon_focus_heavy_pick = 447
feat_weapon_focus_javelin = 435
feat_weapon_focus_kama = 471
feat_weapon_focus_kukri = 468
feat_weapon_focus_light_crossbow = 431
feat_weapon_focus_light_flail = 444
feat_weapon_focus_light_hammer = 437
feat_weapon_focus_light_lance = 439
feat_weapon_focus_light_mace = 423
feat_weapon_focus_light_pick = 440
feat_weapon_focus_longbow = 465
feat_weapon_focus_longspear = 460
feat_weapon_focus_longsword = 446
feat_weapon_focus_morningstar = 428
feat_weapon_focus_net = 486
feat_weapon_focus_nunchaku = 472
feat_weapon_focus_orc_double_axe = 477
feat_weapon_focus_punching_dagger = 421
feat_weapon_focus_quarterstaff = 429
feat_weapon_focus_ranseur = 461
feat_weapon_focus_rapier = 448
feat_weapon_focus_ray = 488
feat_weapon_focus_repeating_crossbow = 485
feat_weapon_focus_sap = 441
feat_weapon_focus_scimitar = 449
feat_weapon_focus_scythe = 462
feat_weapon_focus_short_sword = 442
feat_weapon_focus_shortbow = 463
feat_weapon_focus_shortspear = 430
feat_weapon_focus_shuriken = 483
feat_weapon_focus_siangham = 473
feat_weapon_focus_sickle = 424
feat_weapon_focus_sling = 433
feat_weapon_focus_spike_chain = 478
feat_weapon_focus_spiked_gauntlet = 422
feat_weapon_focus_throwing_axe = 436
feat_weapon_focus_trident = 450
feat_weapon_focus_two_bladed_sword = 480
feat_weapon_focus_unarmed_strike_medium_sized_being = 418
feat_weapon_focus_unarmed_strike_small_being = 419
feat_weapon_focus_warhammer = 451
feat_weapon_focus_whip = 484
feat_weapon_specialization_bastard_sword = 546
feat_weapon_specialization_battleaxe = 515
feat_weapon_specialization_club = 497
feat_weapon_specialization_composite_longbow = 538
feat_weapon_specialization_composite_shortbow = 536
feat_weapon_specialization_dagger = 492
feat_weapon_specialization_dart = 504
feat_weapon_specialization_dire_flail = 551
feat_weapon_specialization_dwarven_urgrosh = 553
feat_weapon_specialization_dwarven_waraxe = 547
feat_weapon_specialization_falchion = 524
feat_weapon_specialization_gauntlet = 489
feat_weapon_specialization_glaive = 526
feat_weapon_specialization_gnome_hooked_hammer = 548
feat_weapon_specialization_grapple = 559
feat_weapon_specialization_greataxe = 527
feat_weapon_specialization_greatclub = 528
feat_weapon_specialization_greatsword = 529
feat_weapon_specialization_guisarme = 530
feat_weapon_specialization_halberd = 531
feat_weapon_specialization_halfling_kama = 539
feat_weapon_specialization_halfling_nunchaku = 541
feat_weapon_specialization_halfling_siangham = 542
feat_weapon_specialization_halfspear = 498
feat_weapon_specialization_hand_crossbow = 554
feat_weapon_specialization_handaxe = 510
feat_weapon_specialization_head = 657
feat_weapon_specialization_heavy_crossbow = 506
feat_weapon_specialization_heavy_flail = 525
feat_weapon_specialization_heavy_lance = 517
feat_weapon_specialization_heavy_mace = 499
feat_weapon_specialization_heavy_pick = 519
feat_weapon_specialization_javelin = 507
feat_weapon_specialization_kama = 543
feat_weapon_specialization_kukri = 540
feat_weapon_specialization_light_crossbow = 503
feat_weapon_specialization_light_flail = 516
feat_weapon_specialization_light_hammer = 509
feat_weapon_specialization_light_lance = 511
feat_weapon_specialization_light_mace = 495
feat_weapon_specialization_light_pick = 512
feat_weapon_specialization_longbow = 537
feat_weapon_specialization_longspear = 532
feat_weapon_specialization_longsword = 518
feat_weapon_specialization_morningstar = 500
feat_weapon_specialization_net = 558
feat_weapon_specialization_nunchaku = 544
feat_weapon_specialization_orc_double_axe = 549
feat_weapon_specialization_punching_dagger = 493
feat_weapon_specialization_quarterstaff = 501
feat_weapon_specialization_ranseur = 533
feat_weapon_specialization_rapier = 520
feat_weapon_specialization_repeating_crossbow = 557
feat_weapon_specialization_sap = 513
feat_weapon_specialization_scimitar = 521
feat_weapon_specialization_scythe = 534
feat_weapon_specialization_short_sword = 514
feat_weapon_specialization_shortbow = 535
feat_weapon_specialization_shortspear = 502
feat_weapon_specialization_shuriken = 555
feat_weapon_specialization_siangham = 545
feat_weapon_specialization_sickle = 496
feat_weapon_specialization_sling = 505
feat_weapon_specialization_spike_chain = 550
feat_weapon_specialization_spiked_gauntlet = 494
feat_weapon_specialization_throwing_axe = 508
feat_weapon_specialization_trident = 522
feat_weapon_specialization_two_bladed_sword = 552
feat_weapon_specialization_unarmed_strike_medium_sized_being = 490
feat_weapon_specialization_unarmed_strike_small_being = 491
feat_weapon_specialization_warhammer = 523
feat_weapon_specialization_whip = 556
feat_whirlwind_attack = 560
feat_wholeness_of_body = 563
feat_widen_spell = 645
feat_wild_shape = 595
feat_woodland_stride = 592

stat_strength = 0
stat_dexterity = 1
stat_constitution = 2
stat_intelligence = 3
stat_wisdom = 4
stat_charisma = 5

stat_ac = 261
stat_age = 233
stat_alignment = 238
stat_alignment_choice = 242
stat_attack_bonus = 266
stat_carried_weight = 268
stat_caster_level = 273
stat_caster_level_barbarian = 274
stat_caster_level_bard = 275
stat_caster_level_cleric = 276
stat_caster_level_druid = 277
stat_caster_level_fighter = 278
stat_caster_level_monk = 279
stat_caster_level_paladin = 280
stat_caster_level_ranger = 281
stat_caster_level_rogue = 282
stat_caster_level_sorcerer = 283
stat_caster_level_wizard = 284
stat_category = 231
stat_cha_mod = 260
stat_con_mod = 257
stat_damage_bonus = 267
stat_deity = 239
stat_dex_mod = 256
stat_domain_1 = 240
stat_domain_2 = 241
stat_experience = 237
stat_favored_enemies = 243
stat_gender = 232
stat_height = 234
stat_hp_current = 229
stat_hp_max = 228
stat_initiative_bonus = 262
stat_int_mod = 258
stat_known_spells = 244
stat_level = 6
stat_level_abjurant_champion = 45
stat_level_arcane_archer = 18
stat_level_arcane_trickster = 19
stat_level_archmage = 20
stat_level_artificer = 44
stat_level_assassin = 21
stat_level_barbarian = 7
stat_level_bard = 8
stat_level_beastmaster = 41
stat_level_blackguard = 22
stat_level_blood_magus = 40
stat_level_bloodclaw_master = 74
stat_level_bloodstorm_blade = 75
stat_level_cerebmancer = 62
stat_level_cleric = 9
stat_level_crusader = 71
stat_level_cryokineticist = 42
stat_level_deepstone_sentinel = 76
stat_level_dragon_disciple = 23
stat_level_druid = 10
stat_level_duelist = 24
stat_level_dwarven_defender = 25
stat_level_eldritch_knight = 26
stat_level_elemental_savant = 39
stat_level_elocator = 63
stat_level_eternal_blade = 77
stat_level_favored_soul = 34
stat_level_fighter = 11
stat_level_frost_mage = 43
stat_level_hierophant = 27
stat_level_horizon_walker = 28
stat_level_iaijutsu_master = 36
stat_level_jade_phoenix_mage = 78
stat_level_loremaster = 29
stat_level_master_of_nine = 79
stat_level_metamind = 64
stat_level_monk = 12
stat_level_mystic_theurge = 30
stat_level_paladin = 13
stat_level_psion = 58
stat_level_psion_uncarnate = 65
stat_level_psionic_fist = 66
stat_level_psychic_warrior = 59
stat_level_pyrokineticist = 67
stat_level_ranger = 14
stat_level_red_avenger = 35
stat_level_rogue = 15
stat_level_ruby_knight_vindicator = 80
stat_level_sacred_fist = 37
stat_level_shadow_sun_ninja = 81
stat_level_shadowdancer = 31
stat_level_slayer = 68
stat_level_sorcerer = 16
stat_level_soulknife = 60
stat_level_stormlord = 38
stat_level_swordsage = 72
stat_level_thaumaturgist = 32
stat_level_thrallherd = 69
stat_level_war_mind = 70
stat_level_warblade = 73
stat_level_warlock = 33
stat_level_wilder = 61
stat_level_wizard = 17
stat_load = 271
stat_melee_attack_bonus = 286
stat_memorized_spells = 245
stat_money = 249
stat_money_cp = 254
stat_money_ep = 252
stat_money_gp = 251
stat_money_pp = 250
stat_money_sp = 253
stat_movement_speed = 269
stat_psi_points_cur = 301
stat_psi_points_max = 300
stat_race = 230
stat_ranged_attack_bonus = 287
stat_run_speed = 270
stat_save_fortitude = 264
stat_save_reflexes = 263
stat_save_willpower = 265
stat_school_prohibited = 248
stat_school_specialization = 247
stat_size = 236
stat_spell_list_level = 288
stat_spells_per_day = 246
stat_str_mod = 255
stat_subdual_damage = 272
stat_subrace = 285
stat_weight = 235
stat_wis_mod = 259

ONF_EX_FOLLOWER = 1
ONF_WAYPOINTS_DAY = 2
ONF_WAYPOINTS_NIGHT = 4
ONF_AI_WAIT_HERE = 8
ONF_AI_SPREAD_OUT = 16
ONF_JILTED = 32
ONF_LOGBOOK_IGNORES = 64
ONF_UNUSED_00000080 = 128
ONF_KOS = 256
ONF_USE_ALERTPOINTS = 512
ONF_FORCED_FOLLOWER = 1024
ONF_KOS_OVERRIDE = 2048
ONF_WANDERS = 4096
ONF_WANDERS_IN_DARK = 8192
ONF_FENCE = 16384
ONF_FAMILIAR = 32768
ONF_CHECK_LEADER = 65536
ONF_NO_EQUIP = 131072
ONF_CAST_HIGHEST = 262144
ONF_GENERATOR = 0x80000
ONF_GENERATED = 0x100000
ONF_GENERATOR_RATE1 = 0x200000
ONF_GENERATOR_RATE2 = 0x400000
ONF_GENERATOR_RATE3 = 0x800000
ONF_DEMAINTAIN_SPELLS = 16777216
ONF_UNUSED_02000000 = 33554432
ONF_UNUSED_04000000 = 67108864
ONF_UNUSED_08000000 = 134217728
ONF_BACKING_OFF = 0x10000000
ONF_NO_ATTACK = 0x20000000
ONF_BOSS_MONSTER = 0x40000000
ONF_EXTRAPLANAR = 0x80000000

OCF_BLINDED = 128
OCF_COMBAT_MODE_ACTIVE = 262144
OCF_ENCOUNTER = 131072
OCF_EXPERIENCE_AWARDED = 4
OCF_FATIGUE_LIMITING = 2147483648L
OCF_FLEEING = 16
OCF_HAS_ARCANE_ABILITY = 256
OCF_IS_CONCEALED = 1
OCF_LIGHT_LARGE = 2097152
OCF_LIGHT_MEDIUM = 1048576
OCF_LIGHT_SMALL = 524288
OCF_LIGHT_XLARGE = 4194304
OCF_MECHANICAL = 536870912
OCF_MONSTER = 32768
OCF_MOVING_SILENTLY = 2
OCF_MUTE = 8192
OCF_NON_LETHAL_COMBAT = 268435456
OCF_NO_FLEE = 134217728
OCF_PARALYZED = 64
OCF_SLEEPING = 4096
OCF_SPELL_FLEE = 65536
OCF_STUNNED = 32
OCF_SURRENDERED = 16384
OCF_UNRESSURECTABLE = 16777216
OCF_UNREVIVIFIABLE = 8388608
OCF_UNUSED_00000008 = 8
OCF_UNUSED_00000200 = 512
OCF_UNUSED_00000400 = 1024
OCF_UNUSED_00000800 = 2048
OCF_UNUSED_02000000 = 33554432
OCF_UNUSED_04000000 = 67108864
OCF_UNUSED_40000000 = 1073741824
