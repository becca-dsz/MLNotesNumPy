<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Machine Learning Notes</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            background-color: #1a1a1a;
            color: #e0e0e0;
            font-family: 'Inter', sans-serif;
        }
        .note-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .note-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-6">
    <div class="w-full max-w-2xl bg-gray-800 rounded-lg shadow-lg p-6">
        <h1 class="text-3xl font-bold text-center text-blue-400 mb-6">Machine Learning Notes</h1>
        
        <!-- Title Input -->
        <div class="mb-4">
            <label for="note-title" class="block text-sm font-medium text-gray-300">Note Title</label>
            <input 
                type="text" 
                id="note-title" 
                placeholder="Enter note title (e.g., Neural Networks Basics)" 
                class="w-full p-3 mt-1 bg-gray-700 border border-gray-600 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500">
        </div>

        <!-- Tags Input -->
        <div class="mb-4">
            <label for="note-tags" class="block text-sm font-medium text-gray-300">Tags (comma-separated)</label>
            <input 
                type="text" 
                id="note-tags" 
                placeholder="e.g., deep learning, python, tensorflow" 
                class="w-full p-3 mt-1 bg-gray-700 border border-gray-600 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500">
        </div>

        <!-- Notes Textarea -->
        <div class="mb-4">
            <label for="note-content" class="block text-sm font-medium text-gray-300">Notes</label>
            <textarea 
                id="note-content" 
                rows="10" 
                placeholder="Write your machine learning notes here..." 
                class="w-full p-3 mt-1 bg-gray-700 border border-gray-600 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>
        </div>

        <!-- Save Button -->
        <div class="flex justify-end">
            <button 
                onclick="saveNote()" 
                class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-md transition duration-200">
                Save Note
            </button>
        </div>

        <!-- Notes Display -->
        <div id="notes-list" class="mt-6">
            <h2 class="text-xl font-semibold text-gray-300 mb-4">Saved Notes</h2>
            <div id="notes-container" class="space-y-4"></div>
        </div>
    </div>

    <script>
        function saveNote() {
            const title = document.getElementById('note-title').value;
            const tags = document.getElementById('note-tags').value.split(',').map(tag => tag.trim());
            const content = document.getElementById('note-content').value;

            if (!title || !content) {
                alert('Please enter a title and content for the note.');
                return;
            }

            // Create note card
            const noteCard = document.createElement('div');
            noteCard.className = 'note-card bg-gray-900 p-4 rounded-md border border-gray-700';
            noteCard.innerHTML = `
                <h3 class="text-lg font-semibold text-blue-400">${title}</h3>
                <p class="text-sm text-gray-400 mb-2">Tags: ${tags.join(', ')}</p>
                <p class="text-gray-200">${content}</p>
            `;

            // Append to notes container
            document.getElementById('notes-container').prepend(noteCard);

            // Clear inputs
            document.getElementById('note-title').value = '';
            document.getElementById('note-tags').value = '';
            document.getElementById('note-content').value = '';
        }
    </script>
</body>
</html>
