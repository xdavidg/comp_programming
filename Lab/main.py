import os
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


def save_middle_axial_slice_nifti(input_filepath, output_image_path):
    """
    Loads a NIfTI file, extracts the middle axial slice, and saves it as an image.

    Args:
        input_filepath (str): Path to the input NIfTI file (.nii or .nii.gz).
        output_image_path (str): Path where the output image will be saved (e.g., .png, .jpg).
    """
    # Load the NIfTI file
    nifti_img = nib.load(input_filepath)
    data = nifti_img.get_fdata()

    # Check if the data has at least 3 dimensions
    if data.ndim < 3:
        raise ValueError("NIfTI file does not have at least 3 dimensions.")

    # Determine the middle slice index along the axial (z) axis
    middle_slice_idx = data.shape[2] // 2

    # Extract the middle axial slice
    middle_slice = data[:, :, middle_slice_idx]

    # Optional: If the data is multi-channel (e.g., RGB), handle accordingly
    if middle_slice.ndim > 2:
        # For simplicity, take the first channel or convert appropriately
        middle_slice = middle_slice[:, :, 0]

    # Normalize the slice to the range [0, 1] for visualization
    slice_min = np.min(middle_slice)
    slice_max = np.max(middle_slice)
    if slice_max - slice_min != 0:
        middle_slice_normalized = (
            middle_slice - slice_min) / (slice_max - slice_min)
    else:
        middle_slice_normalized = middle_slice - slice_min  # All zeros

    # Save the slice using matplotlib
    plt.figure(figsize=(6, 6))
    plt.axis('off')  # Hide axes
    # Transpose for correct orientation
    plt.imshow(middle_slice_normalized.T, cmap='gray', origin='lower')
    plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    print(f"Middle axial slice saved to {output_image_path}")


# Example usage
if __name__ == "__main__":
    # Replace with your NIfTI file path
    input_nifti_path = r"C:\Users\david\OneDrive\Documents\VSCode Programming\Python\Comp498\Lab\T2WI_001.nii"
    # Replace with desired output image path
    output_image_path = r"C:\Users\david\OneDrive\Documents\VSCode Programming\Python\Comp498\Lab\T2WI_001"

    # Ensure the input file exists
    if not os.path.isfile(input_nifti_path):
        raise FileNotFoundError(
            f"Input file {input_nifti_path} does not exist.")

    save_middle_axial_slice_nifti(input_nifti_path, output_image_path)
