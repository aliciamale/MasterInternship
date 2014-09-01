close all
clear all
clc

path = 'MC70/';
name = 'IMG_05';
ext = '.JPG';

for i = 42
    j = int2str(i);
    name_img = strcat(path,name,j,ext);
    nbClass = 6;

    %% Read Image
    I = imread(name_img);
    %figure; subplot(211); imshow(I); title('Image originale');

    %% Convert RGB Image to L*a*b 

    cform = makecform('srgb2lab');
    lab_I = applycform(I,cform);

    %% Classify colors in a*b space using K-means clustering

    ab = double(lab_I(:,:,2:3));
    nrows = size(ab,1);
    ncols = size(ab,2);

    ab = reshape(ab,nrows*ncols,2);

    nColors = nbClass;
    % repeat the clustering 3 times to avoid local minima
    [cluster_id cluster_center] = kmeans(ab,nColors,'distance','sqEuclidean','Replicates',3);

    %% Label Every Pixel in the img using the results from kmeans

    px_label = reshape(cluster_id,nrows,ncols);
    %subplot(212); 
    imshow(px_label,[]); title('Image Labeled by cluster index');
    
    %% Save the image
    
    %name2 = 'IMG_SEGM_05';
    %name_img2 = strcat(path,name2,j,ext);
    %imsave(px_label);
end



