#from jetson_inference import detectNet
#from jetson_utils import videoSource, videoOutput
import jetson.inference
import jetson.utils

# Loading the Detection Model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# # =====================================================
# # Opening the Camera Stream
# camera = jetson.utils.videoSource("/dev/video0")   # '/dev/video0' for V4L2 camera
# display = jetson.utils.videoOutput("display://0")  # 'my_video.mp4' for file output
# # Main Loop: Capture, Detect, and Render
# while display.IsStreaming():
#     img = camera.Capture()
#
#     if img is None:  # capture timeout
#         continue
#
#     detections = net.Detect(img)
#
#     # Print out detection result
#     for d in detections:
#         print(f"ClassID: {d.ClassID}, Confidence: {d.Confidence:.3f}")
#         print(f"Left: {d.Left:.1f}, Top: {d.Top:.1f}, Right: {d.Right:.1f}, Bottom: {d.Bottom:.1f}")
#         print(f"Width: {d.Width:.1f}, Height: {d.Height:.1f}, Area: {d.Area:.1f}")
#         print(f"Center: ({d.Center[0]:.1f}, {d.Center[1]:.1f})\n")
#
#     # Visualize the rendering results
#     display.Render(img)
#     display.SetStatus(f"Object Detection | Network {net.GetNetworkFPS():.0f} FPS")
# # =====================================================

# Specify the path to the image to be detected
image_paths = [
    "/home/nvidia/Desktop/images/test_image1.jpg",
    "/home/nvidia/Desktop/images/test_image2.jpg"
]

# Execute checks on a per-file basis and output the results
for img_path in image_paths:
    print("------------------------------------------------------")
    print(f"Processing image: {img_path}")

    # Load images
    img = jetson.utils.loadImage(img_path)

    # Object detection execution
    detections = net.Detect(img)

    # Output detection results
    for d in detections:
        print(f"ClassID: {d.ClassID}")
        print(f"Confidence: {d.Confidence:.3f}")
        print(f"Left: {d.Left:.3f}, Top: {d.Top:.3f}, Right: {d.Right:.3f}, Bottom: {d.Bottom:.3f}")
        print(f"Width: {d.Width:.3f}, Height: {d.Height:.3f}")
        print(f"Area: {d.Area:.3f}")
        print(f"Center: ({d.Center[0]:.3f}, {d.Center[1]:.3f})\n")

    # Save path for images after generation and detection
    output_path = img_path.replace(".jpg", "_output.jpg")

    # Save the image with the detection box
    jetson.utils.saveImage(output_path, img)

    print(f"Detection result saved to: {output_path}\n")

print("All images processed successfully.")
