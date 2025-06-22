#Text pieces
#First Screen
W1_window_name = "Health"
W1_welcome_text = "Welcome to the Health status detection program!"
W1_instruction_set =(
                        "This application allows you to use the Rufier test to make an initial diagnosis of your health"
                        "The Rufier text is a set of physical exercises designed to assess your cardiac performance during physical exertion"
                        "The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds;"
                        "then, within 45 seconds, the subject performs 30 squats"
                        "When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds"
                        "and then for the last 15 seconds of the first minute of the recovery period."
                        "Important! If you feel unwell during the test (dizziness,"
                        "tinnitus, shortness of breath, etc), stop the test and consult a physician"
                    )
W1_button_text = "Start"

#Second screen
W2_name = "Enter your full name"
W2_age = "Full years"
W2_button1_text = "Start the first test"
W2_button2_text = "Start doing squats"
W2_button3_text = "Start the final test"
W2_button4_text = "Send the results"
W2_instruction1 =( 
                    "Lie on your back and take your pulse for 15 seconds. Click the 'Start first test' button to start the timer"
                    "Write down the result in the appropriate field."
                 )
W2_instruction2 =(
                    "Perform 30 squats in 45 seconds. To do this, click the 'Start doing squats' button"
                    "to start the squat timer."
                 )
W2_instruction3 =(
                    "Lie on your back and take your pulse for 15 seconds. Click the 'Start first test' button to start the timer"
                    "Press the 'Start final test' button to start the timer."
                    "The seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields."
                 )       

#Third screen
W3_window_name = "Results"
W3_Rindex_text = "Roufier Index:"
W3_CPerf_text = "Cardiac performance:"

#Window creation
win_height, win_width = 600, 600
win_move_x, win_move_y = 0, 0