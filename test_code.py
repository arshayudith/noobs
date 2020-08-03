def generate_VI(image,band1,band2):
    """
    This function will calculate the NDVI value from two bands.
    :param image: is the satellite image that will be used for this analysis
    :param band1: is the Red band that extracted from the satellite image
    :param band2: is the NIR band that extracted from the satellite image
    :return: A new numpy array with the same size as the original raster.
    Where all value is the result of mathematical calculation of 'vi'.
    """

    # This block is extracting 1 band from the whole area of the satellite image in float
    imageBand1 = image.GetRasterBand(band1)
    imagePx1 = gdarr.BandReadAsArray(imageBand1, 0, 0, image.RasterXSize, image.RasterYSize)
    imagePx1 = imagePx1.astype(np.float32)
    imageBand1 = None # clean up
    
    # This block is extracting 1 band from the whole area of the satellite image in float
    imageBand2 = image.GetRasterBand(band2)
    imagePx2 = gdarr.BandReadAsArray(imageBand2, 0, 0, image.RasterXSize, image.RasterYSize)
    imagePx2 = imagePx2.astype(np.float32)
    imageBand2 = None # clean up
    
    # This block is do mathematical calculation between extracted 2 bands.
    vi = (imagePx2 - imagePx1) / (imagePx2 + imagePx1)
    imagePx1 = None # clean up
    imagePx2 = None
    return vi

    lalala