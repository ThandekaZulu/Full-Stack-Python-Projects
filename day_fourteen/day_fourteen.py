# from art import higher_lower_game

# output = format_data(game_data.data)
# print(output)

# print(a_followers)
# ........End of Another versio.....
# print(higher_lower_game)
# def format_celebrity(celeb):
#    return f"{celeb['name']}, {celeb['description']}, from {celeb['country']}"

# def game_loop():
#   score = 0

#   random_compare_a = random.choice(game_data.data)
#   random_compare_b = random.choice(game_data.data)

#   while random_compare_b == random_compare_a:
#       random_compare_b = random.choice(game_data.data)

#   while True:
#         print(f"\nCompare A: {format_celebrity(random_compare_a)}")
#         print(f"Compare B: {format_celebrity(random_compare_b)}")
        
#         more_followers_choice = input("Who has more follwers? Type A or B: ").lower()
#         a_followers = random_compare_a["follower_count"]
#         b_followers = random_compare_b["follower_count"]
#         correct = "a" if a_followers > b_followers else "b"

#         if more_followers_choice == correct:
#            score += 1
#            print(f"✅ Correct! Current score: {score}")
#            random_compare_a = random_compare_a if correct == "a" else random_compare_b
#            random_compare_b = random.choice(game_data.data)
#            while random_compare_b == random_compare_a:
#               random_compare_b = random.choice(game_data.data)
#         else:
#            print(f"❌ Wrong! Final score: {score}")
#            break

# game_loop()