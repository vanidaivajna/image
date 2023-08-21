import os
from h2o_wave import main, app, Q, ui

# Paths to the image folders
folder1_path = '/path/to/folder1'
folder2_path = '/path/to/folder2'

# Get image filenames from the folders
folder1_images = [f for f in os.listdir(folder1_path) if f.endswith('.jpg')]
folder2_images = [f for f in os.listdir(folder2_path) if f.endswith('.jpg')]

# Define the Wave app
@app('/image_viewer')
async def serve(q: Q):
    # Initialize the toggle state in q.app
    if not hasattr(q.app, 'toggle'):
        q.app.toggle = False

    # Create a toggle button in a separate form card
    toggle_form = ui.form_card(box='1 1 1 -1', items=[
        ui.toggle(name='toggle', label='Toggle Images', value=q.app.toggle)
    ])

    # Update the toggle state in q.app
    q.app.toggle = q.args.toggle

    # If the toggle button is clicked, update the images
    if q.app.toggle:
        images = folder1_images
        image_path = os.path.join(folder1_path, images[0]) if images else ''
    else:
        images = folder2_images
        image_path = os.path.join(folder2_path, images[0]) if images else ''

    # Set the image path based on the selected folder
    q.app.image = image_path

    # Create the form card to display the image
    image_form_card = ui.form_card(box='2 1 2 -1', items=[
        ui.image(title='Image title', path=q.app.image),
    ])

    # Add the toggle form card and image form card to the page
    q.page['toggle_form'] = toggle_form
    q.page['image_form_card'] = image_form_card

    await q.page.save()
