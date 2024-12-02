import json

def determine_eligibility(input_data):
    """
    Determine eligibility and calculate the Winter Supplement amount.
    Args:
        input_data (dict): JSON data containing client information.
    Returns:
        dict: Output data including eligibility and calculated amounts.
    """
    # Extract input data
    family_comp = input_data["familyComposition"]
    num_children = input_data["numberOfChildren"]
    in_pay = input_data["familyUnitInPayForDecember"]

    # Base eligibility
    is_eligible = in_pay

    # Calculate amounts
    if not is_eligible:
        return {
            "id": input_data["id"],
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0,
        }

    if family_comp == "single":
        base_amount = 60.0
    elif family_comp == "couple":
        base_amount = 120.0
    else:
        raise ValueError("Invalid family composition")

    children_amount = num_children * 20.0
    total_amount = base_amount + children_amount

    return {
        "id": input_data["id"],
        "isEligible": is_eligible,
        "baseAmount": base_amount,
        "childrenAmount": children_amount,
        "supplementAmount": total_amount,
    }
