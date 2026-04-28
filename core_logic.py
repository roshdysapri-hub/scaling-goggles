# [HAI_SYSTEM] - Code 124: Thermal & Logic Synchronization
def analyze_state(temperature, logic_integrity):
    """تحليل العلاقة بين كيمياء الطهي وثبات المنطق التقني"""
    print(f"Testing System at {temperature}C...")
    
    if 140 <= temperature <= 155 and logic_integrity > 0.9:
        return "SUCCESS: Maillard-Logic Sync Achieved."
    elif temperature > 160:
        return "CRITICAL: Thermal Overload. Logic compromised."
    else:
        return "IDLE: Conditions unmet for synchronization."

# محاكاة للنظام
current_status = analyze_state(142, 0.95)
print(f"Current System State: {current_status}")
