import gc
import uasyncio as asyncio
#local imports
import libs.wifi as wifi            # for wifi (network defined in libs/wifi.py)
import libs.download as download    # for downloading the files
import libs.csv as csv              # for time sync and csv interpreting
import libs.general as gen



async def main():
    await wifi.connect()
    await gen.multitask(csv.update_week_vars(), download.download())
    gc.collect()
    

asyncio.run(main())




# old coords

#     start_x = 60  # Ende der Zeitspalte
#     start_y = 40  # Ende des Headers
#     b_w = 148     # Breite einer Box (Box Width)
#     b_h = 38      # Höhe einer Box (Box Height)

#     # --- X-KOORDINATEN (TAGE) ---
#     mo_x = start_x
#     di_x = start_x + b_w
#     mi_x = start_x + 2 * b_w
#     do_x = start_x + 3 * b_w
#     fr_x = start_x + 4 * b_w
#     std_x = 12 

#     # --- Y-KOORDINATEN (STUNDEN) ---
#     h1_y = start_y
#     h2_y = start_y + b_h
#     h3_y = start_y + 2 * b_h
#     h4_y = start_y + 3 * b_h
#     h5_y = start_y + 4 * b_h
#     h6_y = start_y + 5 * b_h
#     h7_y = start_y + 6 * b_h
#     h8_y = start_y + 7 * b_h
#     h9_y = start_y + 8 * b_h
#     h10_y = start_y + 9 * b_h
#     h0_y = 12
    

#     # --- LAYOUT ZEICHNEN ---
#     black_buf.fill(0)
#     red_buf.fill(0)

#     # Weiße Flächen (Invertiert)
#     # black_buf.fill_rect(0, 0, 800, 40, 1)    # Header
#     # black_buf.fill_rect(0, 40, 60, 380, 1)   # Zeitspalte

#     # Horizontale Gitterlinien
#     black_buf.hline(0, h1_y, 800, 1)
#     black_buf.hline(0, h2_y, 800, 1)
#     black_buf.hline(0, h3_y, 800, 1)
#     black_buf.hline(0, h4_y, 800, 1)
#     black_buf.hline(0, h5_y, 800, 1)
#     black_buf.hline(0, h6_y, 800, 1)
#     black_buf.hline(0, h7_y, 800, 1)
#     black_buf.hline(0, h8_y, 800, 1)
#     black_buf.hline(0, h9_y, 800, 1)
#     black_buf.hline(0, h10_y, 800, 1)
#     black_buf.hline(0, 420, 800, 1)

#     # Vertikale Gitterlinien
#     black_buf.vline(mo_x, 0, 420, 1)
#     black_buf.vline(di_x, 0, 420, 1)
#     black_buf.vline(mi_x, 0, 420, 1)
#     black_buf.vline(do_x, 0, 420, 1)
#     black_buf.vline(fr_x, 0, 420, 1)

#     # Tasten-Boxen (7 Stück)
#     black_buf.rect(10, 430, 100, 40, 1)
#     black_buf.rect(122, 430, 100, 40, 1)
#     black_buf.rect(234, 430, 100, 40, 1)
#     black_buf.rect(346, 430, 100, 40, 1)
#     black_buf.rect(458, 430, 100, 40, 1)
#     black_buf.rect(570, 430, 100, 40, 1)
#     black_buf.rect(682, 430, 100, 40, 1)
    
    
# # draw_text_scaled(target_buf, text, x, y, scale, color)

#     draw_text_scaled(black_buf, "MA", mo_x + 8, h1_y + 11, 2, 1)
#     draw_text_scaled(black_buf, "MA", mo_x + 8, h2_y + 11, 2, 1)
#     draw_text_scaled(black_buf, "2.20", mo_x + 105, h1_y + 7, 1, 1)
#     draw_text_scaled(black_buf, "2.20", mo_x + 105, h2_y + 7, 1, 1)
#     draw_text_scaled(black_buf, "Wurm", mo_x + 105, h1_y + 23, 1, 1)
#     draw_text_scaled(black_buf, "Wurm", mo_x + 105, h2_y + 23, 1, 1)
#     # Block 1
#     draw_text_scaled(black_buf, "7:30", std_x, h1_y + 11, 1, 1)
#     draw_text_scaled(black_buf, "8:15", std_x, h2_y + 11, 1, 1)
#     # Block 2
#     draw_text_scaled(black_buf, "9:30", std_x, h3_y + 11, 1, 1)
#     draw_text_scaled(black_buf, "10:15", std_x, h4_y + 11, 1, 1)
#     # Block 3
#     draw_text_scaled(black_buf, "11:30", std_x, h5_y + 11, 1, 1)
#     draw_text_scaled(black_buf, "12:15", std_x, h6_y + 11, 1, 1)
#     # Block 4
#     draw_text_scaled(black_buf, "13:30", std_x, h7_y + 11, 1, 1)
#     draw_text_scaled(black_buf, "14:15", std_x, h8_y + 11, 1, 1)
#     # Block 5
#     draw_text_scaled(black_buf, "15:30", std_x, h9_y + 11, 1, 1)
#     draw_text_scaled(black_buf, "16:15", std_x, h10_y + 11, 1, 1)
    
#     draw_text_scaled(black_buf, "Mo " + datum["mo_akt"], mo_x + 8, h0_y, 2, 1)
#     draw_text_scaled(black_buf, "Di " + datum["di_akt"], di_x + 8, h0_y, 2, 1)
#     draw_text_scaled(black_buf, "Mi " + datum["mi_akt"], mi_x + 8, h0_y, 2, 1)
#     draw_text_scaled(black_buf, "Do " + datum["do_akt"], do_x + 8, h0_y, 2, 1)
#     draw_text_scaled(black_buf, "Fr " + datum["fr_akt"], fr_x + 8, h0_y, 2, 1)
    
    