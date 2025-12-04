# ranking_manager.py
import json
import os

RANKING_FILE = "ranking.json"

def load_ranking():
    if os.path.exists(RANKING_FILE):
        try:
            with open(RANKING_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return [] 
    return []

def save_ranking(ranking_data):
    with open(RANKING_FILE, 'w') as f:
        json.dump(ranking_data, f, indent=4)

def add_score_to_ranking(name, score, level="free"):
    score_updated = False
    ranking = load_ranking()
    for r in ranking:
        if r['name'] == name:
            if score > r['score']:
                r['score'] = score
                score_updated = True
            else:
                score_updated = False 
                ranking.sort(key=lambda x: x['score'], reverse=True)
                save_ranking(ranking)
                
                position = -1
                for i, r_check in enumerate(ranking):
                    if r_check['name'] == name and r_check['level'] == level:
                        position = i + 1
                        break
                return position
            break

    if not score_updated and name not in [e['name'] for e in ranking]:
        new_r = {
            "name": name,
            "score": score,
            "level": level
        }
        ranking.append(new_r)
    ranking.sort(key=lambda x: x['score'], reverse=True)
    ranking = ranking[:10]
    save_ranking(ranking)
    position = -1
    for i, r in enumerate(ranking):
        if r['name'] == name: 
            position = i + 1 
            break
    return position
