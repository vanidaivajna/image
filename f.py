from h2o_wave import main, app, Q, ui

# Define the image paths for both toggle states
image_path_false = '/path/to/image1.jpg'
image_path_true = '/path/to/image2.jpg'

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

    # Determine the image path based on the toggle state
    image_path = image_path_false if not q.app.toggle else image_path_true

    # Create the form card to display the image
    image_form_card = ui.form_card(box='2 1 2 -1', items=[
        ui.image(title='Image title', path=image_path),
    ])

    # Add the toggle form card and image form card to the page
    q.page['toggle_form'] = toggle_form
    q.page['image_form_card'] = image_form_card

    await q.page.save()
