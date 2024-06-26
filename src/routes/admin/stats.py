from flask import flash, redirect, url_for, jsonify
from flask_login import current_user
from models import OperatorManager

def operator_stats():    
    """
    Retrieves the stats of the events of the operator

    Returns:
        The stats representing the percentage of events in the morning and in the afternoon 
    """
  
    if not current_user.get_privilege():
        flash("You are not an operator at the moment", "error")
        return redirect(url_for('main.login'))
    
    operator = OperatorManager().get(current_user.get_id())

    morning = 0
    afternoon = 0
    events = operator.getAllEvents()

    for event in events:
        if event.getTimeSpan()[1] < 1200:
            morning += 1
        else:
            afternoon += 1
    morning = float(f'{morning/len(events):.2f}') * 100
    afternoon = float(f'{afternoon/len(events):.2f}') * 100
    if morning + afternoon < 100:
        morning += 100 - (morning + afternoon)
    
    return jsonify({'morning' : f'{morning:.2f}', 'afternoon': f'{afternoon:.2f}'}), 200
