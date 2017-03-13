from fiber_properties import ImageAnalysis, image_list, show_image_array

folder = '../data/scrambling/2016-08-05 Prototype Core Extension 1/'
dark_folder = folder + 'Dark/'
ambient_folder = folder + 'Ambient/'

in_images = image_list(ambient_folder + 'in_')
nf_images = image_list(ambient_folder + 'nf_')
ff_images = image_list(ambient_folder + 'ff_')

print 'input'
for image in in_images:
    print ImageAnalysis(image, ambient=in_images).get_fiber_centroid(method='full')
print
print 'near field'
for image in nf_images:
    nf_obj = ImageAnalysis(image, camera='nf')
    print nf_obj.get_fiber_centroid(method='full', units='microns')
print
print 'far field'
for image in ff_images:
    ff_obj = ImageAnalysis(image, camera='ff')
    print ff_obj.get_fiber_centroid(method='full', units='microns')