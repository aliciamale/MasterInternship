clear all
close all
clc

I = imread('IMG_0533.JPG');
figure;

% for n = 3:6
%     Idx = otsu(I,n);
%     i = n-2;
%     subplot(2,2,i);
%     imagesc(Idx);
%     title(['Image Segmentee, n = ', num2str(n)]);
% end

Idx = otsu(I,3);
imagesc(Idx);

figure;
Idx = otsu(I,4);
imagesc(Idx);

figure;
Idx = otsu(I,5);
imagesc(Idx);

figure;
Idx = otsu(I,6);
imagesc(Idx);