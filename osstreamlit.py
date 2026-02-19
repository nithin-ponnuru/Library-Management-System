import streamlit as st
import matplotlib.pyplot as plt
from collections import deque, Counter
import random

st.set_page_config(page_title="Page Replacement Algorithm Simulator", layout="wide")

st.title("📊 Page Replacement Algorithm Simulator")

# FIFO Page Replacement Algorithm
def fifo(pages, frames):
    memory, page_faults, page_hits = deque(), 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                memory.popleft()
            memory.append(page)
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# LRU Page Replacement Algorithm
def lru(pages, frames):
    memory, page_faults, page_hits = [], 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
            memory.remove(page)
        else:
            page_faults += 1
            if len(memory) == frames:
                memory.pop(0)
        memory.append(page)
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# LFU Page Replacement Algorithm
def lfu(pages, frames):
    memory, freq, page_faults, page_hits = [], Counter(), 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                least_used = min(memory, key=lambda p: freq[p])
                memory.remove(least_used)
            memory.append(page)
        freq[page] += 1
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# MFU Page Replacement Algorithm
def mfu(pages, frames):
    memory, freq, page_faults, page_hits = [], Counter(), 0, 0
    frame_updates = []
    for page in pages:
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                most_used = max(memory, key=lambda p: freq[p])
                memory.remove(most_used)
            memory.append(page)
        freq[page] += 1
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    return page_faults, page_hits, frame_updates

# Optimal Page Replacement Algorithm
def optimal(pages, frames):
    memory, page_faults, page_hits = [], 0, 0
    frame_updates = []
    
    for i, page in enumerate(pages):
        if page in memory:
            page_hits += 1
        else:
            page_faults += 1
            if len(memory) == frames:
                future_use = {}
                for mem_page in memory:
                    try:
                        future_use[mem_page] = pages[i+1:].index(mem_page)
                    except ValueError:
                        future_use[mem_page] = float('inf')
                page_to_replace = max(future_use, key=future_use.get)
                memory.remove(page_to_replace)
            memory.append(page)
        
        frame_updates.append(f"{page} : {' '.join(map(str, memory))}")
    
    return page_faults, page_hits, frame_updates

# Plotting results
def plot_results(results):
    labels, faults, hits = zip(*[(algo, faults, hits) for algo, faults, hits, _ in results])
    
    fig, ax = plt.subplots()
    ax.bar(labels, faults, label='Page Faults')
    ax.bar(labels, hits, bottom=faults, label='Page Hits')
    ax.set_xlabel("Algorithms")
    ax.set_ylabel("Counts")
    ax.set_title("Page Replacement Algorithm Comparison")
    ax.legend()
    st.pyplot(fig)

# ================= STREAMLIT INPUT =================

length = st.number_input("Enter the length of the trace:", min_value=1, step=1)

manual = st.radio("Do you want to enter pages manually?", ["Yes", "No"])

if manual == "Yes":
    page_input = st.text_input("Enter space-separated page references:")
    if page_input:
        pages = list(map(int, page_input.replace(",", " ").split()))
    else:
        pages = []
else:
    if length > 0:
        pages = [random.randint(1, 10) for _ in range(length)]
        st.write("Generated Page References:", pages)
    else:
        pages = []

frames = st.number_input("Enter the number of frames:", min_value=1, step=1)

algorithm_options = {
    "FIFO": fifo,
    "LRU": lru,
    "LFU": lfu,
    "MFU": mfu,
    "OPTIMAL": optimal
}

selected_algos = st.multiselect(
    "Select Algorithms to Run:",
    ["FIFO", "LRU", "LFU", "MFU", "OPTIMAL"]
)

if st.button("Run Simulation"):

    if not pages or frames == 0 or not selected_algos:
        st.warning("Please enter valid inputs and select at least one algorithm.")
    else:
        results = []

        for name in selected_algos:
            func = algorithm_options[name]
            faults, hits, frame_updates = func(pages, frames)
            results.append((name, faults, hits, frame_updates))

        for name, faults, hits, frame_updates in results:
            total = faults + hits
            st.subheader(f"{name} Algorithm")

            for update in frame_updates:
                st.text(update)

            st.write(f"Page Faults: {faults}")
            st.write(f"Page Hits: {hits}")
            st.write(f"Miss Ratio: {faults / total:.2%}")
            st.write(f"Hit Ratio: {hits / total:.2%}")

        plot_results(results)
