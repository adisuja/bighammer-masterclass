# Cognitive-walkthrough simulation: 100 simulated visitors, each drawn from an archetype.
# The archetype mix and "patience" are ASSUMPTIONS (stated below). The page facts are MEASURED in the browser.
import random, json, sys
random.seed(7)
ARCH = [  # name, count, device, patience_screens, needs
 ("Mobile LinkedIn skimmer",        22, "m", 1.5, {"form_first_screen","date_free"}),
 ("Mobile engaged data leader",     18, "m", 5.0, {"form_reach","proof","agenda"}),
 ("Desktop high-intent (email/ref)",14, "d", 1.0, {"form_first_screen","date_free"}),
 ("Desktop evaluator",              14, "d", 5.0, {"form_reach","hosts_cred","agenda"}),
 ("FinOps / finance owner",          8, "d", 8.0, {"proof","form_reach"}),
 ("Skeptic (wants named proof)",     8, "d", 6.0, {"named_proof","hosts_cred"}),
 ("Privacy-cautious",                6, "m", 3.0, {"form_reach","low_ask"}),
 ("Timezone planner",                6, "m", 2.0, {"local_time","date_free"}),
 ("Curious non-buyer",               4, "d", 1.0, set()),
]
def run(facts):
    blocked = {}
    ex = {}
    for name,n,dev,pat,needs in ARCH:
        f = facts[dev]
        for _ in range(n):
            hit=[]
            if "form_first_screen" in needs and not f["submit_in_first_screen"]: hit.append("Cannot register without scrolling")
            if "form_reach" in needs and f["screens_to_submit"]>pat: hit.append("Form out of reach in their scroll budget")
            if "date_free" in needs and not f["date_free_in_first_screen"]: hit.append("Date or price not visible at first glance")
            if "local_time" in needs and not f["local_time_in_first_screen"]: hit.append("Own-timezone time not visible early")
            if "hosts_cred" in needs and f["screens_to_hosts"]>pat: hit.append("Host credibility not reached in budget")
            if "proof" in needs and f["screens_to_proof"]>pat: hit.append("Proof not reached in budget")
            if "named_proof" in needs: hit.append("No named customer logos to check")
            if "agenda" in needs and f["screens_to_agenda"]>pat: hit.append("Agenda not reached in budget")
            if "low_ask" in needs and f["required_fields"]>3: hit.append("Too many required fields")
            for h in hit: ex[h]=ex.get(h,0)+1
            if hit: blocked[name]=blocked.get(name,0)+1
    return ex, blocked
json.dump(ARCH, open("arch.json","w"), default=list)
before = json.load(open(sys.argv[1]))
ex, blocked = run(before)
print("visitors hitting at least one friction:", sum(blocked.values()), "of 100")
for k,v in sorted(ex.items(), key=lambda x:-x[1]): print(f"{v:3d}  {k}")
