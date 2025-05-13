import pygame

def url_animation_of(entity):  # KHAI BÁO HÀM LẤY URL THƯ VIỆN ANIMATION KHI CHỌN VẬT THỂ
    url_path = "bin\\packages\\texture\\" + entity
    return url_path

def animation_path_frames(urlpath, w_e, h_e, status):
    geturl = ""
    image = ""
    try:
        geturl = url_animation_of(urlpath+"\\"+status+".png")
        
        image = pygame.image.load(geturl).convert_alpha()
    except:
        geturl = url_animation_of("NULL\\"+status+".png")
        image = pygame.image.load(geturl).convert_alpha()
    print(image)
    frames = []  # khung hình nhập vào
    sheet_width = image.get_width()
    for i in range(sheet_width // w_e):  # vòng lặp lấy hình và add vào chuỗi
        frame = image.subsurface(pygame.Rect(i * w_e, 0, w_e, h_e))
        frames.append(frame)
    return frames



class entity_lifes(): #KHAI BÁO HÀM TẠO 1 VẬT THỂ - CÓ SỰ SỐNG (CÓ THỂ DI CHUYỂN)
	def __init__(entity_id, x, y,width_e,height_e ,entity_name, pic_per_sec): #KHAI HÀM GỌI NHÂN VẬT VÍ DỤ (GÁN VẬT THỂ A, CÓ TỌA ĐỘ X,Y ,CAO,RỘNG, TÊN VẬT THỂ LÀ VILLAGE) THÌ SẼ CÓ LỆNH SAU entity_lifes(A,20,20,128,128,"Village") và sẽ tạo vật thể như sau lên màn hình trò chơi
 		entity_id.x = x #TỌA ĐỘ
 		entity_id.y = y #TỌA ĐỘ
 		entity_id.animations_types = {#LẤY FRAMES / FRAME LÀ 1 TẤM HÌNH TRONG CHUỖI FRAMES NHƯNG DO NHIỀU ANINMATION KHÁC NHAU NÊN SẼ CÓ CÁC PHẦN KHÁC NHAU
 			"dungyen": animation_path_frames(entity_name,width_e,height_e,"dungyen"),
 			"dibo": animation_path_frames(entity_name,width_e,height_e,"dibo"),
 			"chay": animation_path_frames(entity_name,width_e,height_e,"chay"),
 			"healing": animation_path_frames(entity_name,width_e,height_e,"ancomchien"),
 			"nhatdo": animation_path_frames(entity_name,width_e,height_e,"nhatdo"),
 			"chet": animation_path_frames(entity_name,width_e,height_e,"die"),
 			"danhnhau_danh": animation_path_frames(entity_name,width_e,height_e,"danh"),
 			"danhnhau_ban": animation_path_frames(entity_name,width_e,height_e,"ban")
 		}
 		entity_id.animation_type = "dungyen" #TÊN ANIMATION SẼ DIỄN RA
 		entity_id.frame_offical_index = 0 #SỐ THỨ TỰ FRAME TỪ BAN ĐẦU 
 		entity_id.animation_speed = pic_per_sec #TỐC ĐỘ KHUNG HÌNH CHO ANIMATION
 		entity_id.offical_time = 0 #THỜI GIAN ĐÃ QUA CỦA ENTITY KHI THỰC HIỆN ANIMATION
 		entity_id.frame_index = entity_id.animations_types[entity_id.animation_type] #LẤY ANIMATION TỪ FRAME ĐÃ CHỌN
 		entity_id.frame_action_index = entity_id.frame_index[0] #THỰC HIỆN SẼ SỬ DỤNG ANIMATION SAU KHI ĐẴ LẤY

	def changing_animation(entity_id,name_animation):  #BIẾN ĐỔI ANIMATION
 		if name_animation!=entity_id.animation_type:
 			entity_id.animation_type = name_animation
 			entity_id.frame_index = entity_id.animations_types[entity_id.animation_type]
 			entity_id.offical_time = 0
 			entity_id.frame_offical_index = 0
			
 			

	def update(entity_id, animation_time):          #BIẾN UPDATE ANIMATION THEO TĂNG DẦN CỦA entity_id.offical_time và entity_id.frame_offical_index 
	    entity_id.offical_time += animation_time
	    if entity_id.offical_time >= entity_id.animation_speed:
	        entity_id.offical_time = 0
	        entity_id.frame_offical_index = (entity_id.frame_offical_index + 1) % len(entity_id.frame_index)
	        entity_id.frame_action_index = entity_id.frame_index[entity_id.frame_offical_index]

	def draw(entity_id, surface):                      #VẼ FRAME.
		surface.blit(entity_id.frame_action_index, (entity_id.x, entity_id.y))
