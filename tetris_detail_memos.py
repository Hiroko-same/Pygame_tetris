#-- ランダムな動きが必要なTetris game--
  Pygameのシステムを使用
  自作モジュールを使用
  Pygameの初期化
# -- Random movement in Tetris game --
  Use the Pygame library system.
  Initialize Pygame.
  The game moves blocks randomly.


#-- グリッドの設定--
  列数,行数
  １マスのサイズ（ピクセル）
  Windowサイズ（マス数＊サイズ）
  色設定
# -- Grid setup --
  Number of columns and rows.
  Cell size in pixels.
  Set up the grid for the Tetris field.
  Define the window size = (number of cells) × (cell size).
  Define colors to be used in the game.
  Setup of colors.


#-- Window作成--
  横に余白を作成
  Tetris画面の横に余白をセットする
  タイトルはTetris
  フォント(フォント種類は指定なし、サイズは36)
# -- Window creation --
  Create a margin on the right side of the Tetris screen.
  The window title is “Tetris”.
  Set up the font (type unspecified, size = 36).


#-- ブロックの初期位置--
  左から５列目(0始まり)
  上から１行目
# -- Initial block position --
  Start from the 5th column from the left (index starts at 0).
  1st row from the top.


#-- 時間管理用/ゲーム用変数--
  ループすることで時間経過を再現する関数
  0.5秒ごとに落ちる
  ゲーム開始時からの時間をミリ秒で(tick)返す関数
  スコアカウントは０でスタート、ゲームオーバーの場合はFalseを返す
# -- Time management & game variables --
  Use a loop function to simulate time progression.
  Blocks drop every 0.5 seconds.
  A function returns the elapsed time in milliseconds (tick).
  Score starts from 0, and when the game is over, it returns False.


#-- フィールド（地面:0は空き）--
  10列(cols)分０を書く、それを20行(rows)分繰り返す,0でフィールドを埋める
# -- Field (ground: 0 = empty) --
  Create 10 columns filled with 0, repeated for 20 rows.
  Fill the entire field with 0 to represent empty space.


#-- テトリミノの定義--
  テトリミノの形状の定義
# -- Definition of Tetrominoes --
  Define all Tetromino shapes.


#-- テトリミノの形状の選び方や位置などの初期化--
　 ランダムな新しいテトリミノを出現させる
　 (x, y)の初期位置は10列(cols)の中心かつ、1行目(rows)
　 new_block()関数の結果を current_block とする
# -- Initialize Tetromino position and selection --
  Randomly spawn a new Tetromino.
  The initial position (x, y) is at the center of the 10 columns, and 1st row.
  The result of the new_block() function becomes current_block.

#--グリッドを描く関数(表の中のマス目を描く）--
  行と列の交差のマス目ごとに指定のサイズの四角を設定
  グレーの線で四角を描く
  線だけ描く（塗りつぶさない）
# -- Function to draw the grid (lines of the field) --
  Draw rectangles of the specified cell size at the intersection of rows and columns.
  Use gray lines to draw the grid.
  Draw only the outline (no fill).

#--最新のブロックを描く--
  current_blockの最新位置の計算（座標は動き続けるのでdx,dyを使用して計算）
  current_blockの形を作るための座標current_block['x']['y']に動かす先の座標dx,dyを加算
  Tetrisの画面から位置座標が外れなければ、四角で形状を作成、ブロックをCYANで塗りつぶす
# -- Draw the current block --
  Calculate the current position of current_block using dx and dy (because the block keeps moving).
  Add the destination offset (dx, dy) to the coordinates of the current_block['x']['y'] to form its shape.
  If the position is within the Tetris display, draw rectangles filled with CYAN to represent the block.

#-- 地面を描く--
  行と列の交差マスの座標が0以外の場合、そのマスに四角を描く
  ブロックをCYANで塗りつぶす
# -- Draw the field (grounded blocks) --
  For each cell that is non-zero, draw a rectangle in that position.
  Fill the block with CYAN color.

#-- ブロックが動けるかチェック--
  ブロックをdx,dyの位置に動かしたときのpx,py（停止している座標）を計算
  Tetrisの画面上からはみ出した時Falseを返す
  落下時にy座標が０以上でかつ何かにぶつかった時False
  Falseを返すとcan_move()は停止
# -- Check if the block can move --
  Calculate the new position (px, py) of the block after moving to (dx, dy).
  Return False if the block goes outside the Tetris display area.
  Also return False if the block's y position is ≥ 0 and it collides with another block when falling.
  If False is returned, the can_move() function stops.

#--回転の為の関数--
  O型は回転しない
  90度時計回り
 （（x,y）⇒（-y,x）にしたいので、for文でcurrent_block['shape']内の全ての座標に(-py,px)を代入）
  形を変えたブロックを返す

# -- Function for rotation --
  The O-shaped Tetromino does not rotate.
  Rotate the block 90° clockwise.
  For every coordinate (x, y) inside current_block['shape'], transform it to (-y, x) for rotation.
  Return the new shape.

#--ブロックをフィールドに固定--
  ブロックが動いている位置を計算して割り出す
  ブロックの位置座標がTetris画面内ならフィールド上のマス目を１で埋める
  ブロックを地面の一部とする
# -- Lock the block on the field --
  Calculate the current moving position of the block.
  If the block’s position is within the game field, fill that cell with 1.
  This makes the block become part of the grounded field.

#--揃った行を消す処理--
  while文外にあるfield,scoreを計算できるようにする
  もし1つでも行の中のマスが0＝空ならフィールド上の行はそのままの形で全行を埋める
  全フィールドの行数からnew_field分の行数を引いた値(空のマスがある行は差なし)をlines_clearedとする
  scoreはlines_cleared*100とする
  lines_clearedの数字分、new_fieldの0番目に列分のマスを０で埋めたものを入れる、を繰り返す
  new_fieldをfieldとする
# -- Erase completed lines --
  Allow field and score to be calculated outside the while loop.
  For each row:
    If any cell is 0, keep the row as is.
  Otherwise, it’s considered a completed line.
  lines_cleared = total field rows − number of rows in the new field (new_field).
  score increases by lines_cleared × 100.
  For each cleared line, insert a new empty row (filled with 0) at the top of new_field.
  Finally, set field = new_field.

# -- ゲームオーバー判定--
#　１行目（field[0][x]）の１０列のうち、どれか１つでも０以外で埋まっている場合、ゲームオーバーと判定する
# -- Game over condition --
  Check the top row (field[0][x]).
  If any of the 10 cells in the top row (field[0][x]) are non-zero, return a Game Over state.

# --次のブロック表示の文字--   
  文字はNEXT、白い文字
  スクリーン上にnext_textを表示するブロックを作成（左辺：WIDTH＋20、上辺：20）
  次に表示するブロックの「shape」を構成する全ての座標について、移動先座標dx,dyを計算
  xはWIDTH+40に移動先のx座標＊マスサイズ分が加算される
  yは60＋移動先のy座標＊マスサイズ分が加算される
# -- Display the next block text --
  Display the label “NEXT” in white color.
  Create a text area for next_text on the screen:
    Left: WIDTH + 20
    Top: 20
  Calculate the destination coordinates (dx, dy) for all parts of the next block’s shape.
  Set each shape’s position:
    x = WIDTH + 40 + (dx × cell size)
    y = 60 + (dy × cell size)

#-- ゲーム初期化に必要な変数--
　テトリスゲームをスタートするために欠かせない全変数を定義
# -- Variables for initializing the game --
  Define all variables necessary to start the Tetris game.

#-- メインループ--
　 イベントタイプがQUITならシステムの終了
　 キー操作
  can_move()にcurrent_blockの['x']['y']とnew_shapeを代入し、
  移動座標は動かさず(dx=0,dy=0)にcurrent_blockを90度回転させる（rotate()）
  回転させたnew_shape（current_block）をcurrent_block['shape']に代入
# -- Main loop --
  If the event type is QUIT, exit the game system.
  Keyboard operations.
  Call can_move() with current_block['x'], current_block['y'], and new_shape.
  If rotation is triggered, keep the position fixed (dx = 0, dy = 0) and rotate current_block by 90° using rotate().
  Then assign the rotated new_shape to current_block['shape'].


# --ゲームオーバーじゃない時--
  自動落下の設定にする
  current_timeにゲーム内の時間をミリ秒で(tick)返す関数を代入
  最新の経過時間（ミリ秒）から最初の経過時間（ミリ秒）の差異が落下時間（500ミリ秒）より多い時、
  can_move()にdx=0,dy=1でcurrent_blockが代入できる場合はcurrent_blockの['y']とscoreに1を加算、
  それが代入できない時は、lock_block()を用いる
  lock_block()にcurrent_blockを代入し、clear_lines()で揃った行を消す
  １行目（field[0][x]）の１０列のうち、どれか１つでも０以外で埋まっている場合
  gameover=Trueを返す
  それ以外のときはゲーム初期化に必要な変数を代入
  1つのブロックの処理が終わったら、last_fall_timeを更新（current_timeをlast_fall_timeに代入）
# -- When the game is not over --
  Enable automatic falling of blocks.
  Assign current_time to the current game time in milliseconds (using tick()).
  If the difference between current_time and last_fall_time is greater than 500 ms,
  and if can_move(dx=0, dy=1) returns True → move the block down and increase the score by 1.
  If not → call lock_block() to fix the block on the field.
  Then call clear_lines() to remove any completed lines.
  If any cell in the top row (field[0][x]) is non-zero, set gameover = True.
  Otherwise, initialize a new block for the next round.
  After processing one block, update last_fall_time = current_time.
 
# --ゲーム起動中の流れ--
# 画面の背景色は黒
# gridやfieldが描かれる
# ゲームオーバーでない時はdraw_block()にcurrent_blockを代入して最新のブロックを画面上に描く
# score表示、文字表示に必要な要素は「表示したいテキストScore:スコア数、ゲームオーバーじゃない時True、白色」
# f-stringsはf{}内に変数やPythonの式を直接埋め込める機能
# 画面上にscore_textを入れる画面を作成（左辺：WIDTH＋20、上辺：HEIGHT-50）
# NEXTブロックを本体画面横に表示させる（draw_next_block()にnext_blockを代入）
# -- During the game (main display loop) --
  The background color of the screen is black.
  Draw both the grid and field.
  If the game is not over, call draw_block(current_block) to display the current falling block.
  Show the score text:
    Text: Score: {score}
    Color: white
  Display position: (left = WIDTH + 20, top = HEIGHT - 50)
  Use an f-string (f"{variable}") to embed Python expressions directly in strings.
  Show the NEXT block beside the main field by calling draw_next_block(next_block).


# --ゲームオーバー表示--
# ゲームオーバーになったらテキスト表示、文字表示に必要な要素は「テキスト”ゲームオーバー”、ゲームオーバーである時True,白色」
# over_textを表示させる場所を画面上に作成（左辺：WIDTHの半分、上辺：HEIGHTの半分-20）
# -- Game Over display --
  When the game is over, display the text: “GAME OVER” in white.
  Create a text area for over_text on the screen:
    Left: half of WIDTH
    Top: half of HEIGHT - 20


# --ゲーム起動中の画面更新--
# pygame.display.flip()でpygame.display.set_mode()で表示させた画面全体をまるごと更新
# 1秒間に60回以内の画面更新までに制限する（それ以上速い速度でゲームが更新されないようにする））
# -- Screen update during the game --
  Use pygame.display.flip() to refresh the entire screen created by pygame.display.set_mode().
  Limit the screen refresh rate to a maximum of 60 frames per second,
  to prevent the game from running too fast.


