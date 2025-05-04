#!/usr/bin/env python3

def ask(prompt):
    response = input(f"{prompt}\n> ")
    return response.strip().lower()

print("\n🧭 Neuro-Spicy Mode Self-Mapping Tool")
print("Find your quadrant. Meet your kind.\n")

# Emotional Output Questions
print("🔥 Emotional Output Style:")
eo_answers = [
    ask("When you feel something big, what does it look like?"),
    ask("Do people say you're too much, too emotional, or dramatic? (yes/no)"),
    ask("Do you cry, laugh, or express emotion easily and loudly? (yes/no)"),
    ask("Do you hold things in or express indirectly? (yes/no)"),
]

# Masking History Questions
print("\n💬 Social Masking History:")
sm_answers = [
    ask("Have you built a persona to survive? (yes/no)"),
    ask("Do you change depending on who you’re with? (yes/no)"),
    ask("Do you struggle to hide your feelings, even when you try? (yes/no)"),
    ask("Has unmasking been recent and painful? (yes/no)"),
]

# Analyze responses
explosive_score = eo_answers[:3].count("yes")
dripping_score = eo_answers[3:].count("yes")
compartmentalized_score = 4 - (explosive_score + dripping_score)

mask_score = sm_answers[:1].count("yes") * 2 + sm_answers[1:].count("yes")

if explosive_score >= 2:
    style = "Explosive"
elif dripping_score >= 1:
    style = "Dripping"
else:
    style = "Compartmentalized"

if mask_score >= 4:
    mask = "High Masker"
elif mask_score >= 2:
    mask = "Adaptive Masker"
else:
    mask = "Raw Signal"

# Determine alignment type
alignments = {
    ("Explosive", "High Masker"): "⚡ Volcano Heart",
    ("Explosive", "Adaptive Masker"): "🎧 Emotional DJ",
    ("Explosive", "Raw Signal"): "🎙️ Walking Broadcast",
    ("Dripping", "High Masker"): "📓 Ghost Writer",
    ("Dripping", "Adaptive Masker"): "🧪 Social Alchemist",
    ("Dripping", "Raw Signal"): "🪶 Soft Siren",
    ("Compartmentalized", "High Masker"): "🧱 Ice Fortress",
    ("Compartmentalized", "Adaptive Masker"): "🌀 Hidden Whirlpool",
    ("Compartmentalized", "Raw Signal"): "🌫️ Soul Window",
}

alignment = alignments.get((style, mask), "Unclassified Neuro-Spicy")

# Result
print(f"\n🧠 Your Emotional Output Style: {style}")
print(f"🎭 Your Masking Style: {mask}")
print(f"✨ Neuro-Spicy Alignment: {alignment}")
print("\nVisit the Neuro-Spicy Mode chart to explore your quadrant deeper.")
