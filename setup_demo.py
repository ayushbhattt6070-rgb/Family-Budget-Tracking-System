# setup_demo.py
import auth_app
import data_handler
import visualize


NUM_USERS = 50
FAMILY_COUNT = 5

print("🔹 Step 1: Initializing Database...")
auth_app.init_db()
print("✅ Database Initialized")

print(f"🔹 Step 2: Generating {NUM_USERS} Users across {FAMILY_COUNT} Families...")
auth_app.auto_generate_users(n=NUM_USERS, family_count=FAMILY_COUNT)
print("✅ Users Generated")

print("🔹 Step 3: Generating Expenses for all users...")
data_handler.auto_generate_expenses(family_count=FAMILY_COUNT)
print("✅ Expenses Generated")

print("🔹 Step 4: Generating Charts")
for f in range(1, FAMILY_COUNT + 1):
    family_id = f"fam" + str(f)
    visualize.bar_chart_family(family_id)

print("✅ Charts")

print("\n🎉 Setup Complete! You can now run `python app.py` to launch the dashboard.")
