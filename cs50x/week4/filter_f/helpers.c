#include <math.h>
#include <stdlib.h>
#include "helpers.h"


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE pixel[height][width];

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            pixel[i][j] =  image[i][j];
            int gray = (pixel[i][j].rgbtBlue + pixel[i][j].rgbtBlue + pixel[i][j].rgbtBlue) / 3;
            pixel[i][j].rgbtBlue = gray;
            pixel[i][j].rgbtRed = gray;
            pixel[i][j].rgbtGreen = gray;
        }
    }

    for(int q = 0; q < height; q++)
    {
        for(int e = 0; e < width; e++)
        {
            image[q][e] = pixel[q][e];
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE reflect = image[i][width - j];
            image[i][width - j] = image[i][j];
            image[i][j] = reflect;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE pixel[height][width];

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {

            int h1 = i-1;
            int h2 = i+1;
            int w1 = j-1;
            int w2 = j+1;

            if(h1 < 0)
            {
                h1 = i;
            }
            if(w1 < 0)
            {
                w1 = j;
            }
            if(h2 > height)
            {
                h2 = i;
            }
            if(w2 > width)
            {
                w2 = j;
            }

            pixel[i][j] =  image[i][j];
            RGBTRIPLE pixel_1 =  image[h1][w1];
            RGBTRIPLE pixel_2 =  image[h1][j];
            RGBTRIPLE pixel_3 =  image[h1][w2];
            RGBTRIPLE pixel_4 =  image[i][w1];
            RGBTRIPLE pixel_5 =  image[i][w2];
            RGBTRIPLE pixel_6 =  image[h2][w1];
            RGBTRIPLE pixel_7 =  image[h2][j];
            RGBTRIPLE pixel_8 =  image[h2][w2];

            int a_rgbtRed = (pixel_1.rgbtRed + pixel_2.rgbtRed + pixel_3.rgbtRed + pixel_4.rgbtRed + pixel_5.rgbtRed + pixel_6.rgbtRed + pixel_7.rgbtRed + pixel_8.rgbtRed + pixel[i][j].rgbtRed) / 9;
            int a_rgbtGreen = (pixel_1.rgbtGreen + pixel_2.rgbtGreen + pixel_3.rgbtGreen + pixel_4.rgbtGreen + pixel_5.rgbtGreen + pixel_6.rgbtGreen + pixel_7.rgbtGreen + pixel_8.rgbtGreen + pixel[i][j].rgbtGreen) / 9;
            int a_rgbtBlue = (pixel_1.rgbtBlue + pixel_2.rgbtBlue + pixel_3.rgbtBlue + pixel_4.rgbtBlue + pixel_5.rgbtBlue + pixel_6.rgbtBlue + pixel_7.rgbtBlue + pixel_8.rgbtBlue + pixel[i][j].rgbtBlue) / 9;
            pixel[i][j].rgbtBlue = a_rgbtBlue;
            pixel[i][j].rgbtRed = a_rgbtRed;
            pixel[i][j].rgbtGreen = a_rgbtGreen;
        }
    }

    for(int q = 0; q < height; q++)
    {
        for(int e = 0; e < width; e++)
        {
            image[q][e] = pixel[q][e];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int h1 = i-1;
            int h2 = i+1;
            int w1 = j-1;
            int w2 = j+1;

            if(h1 < 0)
            {
                h1 = 0;
            }
            if(w1 < 0)
            {
                w1 = 0;
            }
            if(h2 > height)
            {
                h2 = height - 1;
            }
            if(w2 > width)
            {
                w2 = width - 1;
            }

            temp[i][j] =  image[i][j];
            RGBTRIPLE pixel_1 =  image[h1][w1];
            RGBTRIPLE pixel_2 =  image[h1][j];
            RGBTRIPLE pixel_3 =  image[h1][w2];
            RGBTRIPLE pixel_4 =  image[i][w1];
            RGBTRIPLE pixel_5 =  image[i][w2];
            RGBTRIPLE pixel_6 =  image[h2][w1];
            RGBTRIPLE pixel_7 =  image[h2][j];
            RGBTRIPLE pixel_8 =  image[h2][w2];

            int gx_red = (pixel_1.rgbtRed * -1) + (pixel_3.rgbtRed * 1) + (pixel_4.rgbtRed * -2) + (pixel_5.rgbtRed * 2) + (pixel_6.rgbtRed * -1) + (pixel_8.rgbtRed * 1);
            int gy_red = (pixel_1.rgbtRed * -1) + (pixel_2.rgbtRed * -2) + (pixel_3.rgbtRed * -1) + (pixel_6.rgbtRed * 1) + (pixel_7.rgbtRed * 2) + (pixel_8.rgbtRed * 1);
            gx_red = abs(gx_red);
            gy_red = abs(gy_red);
            int sobel_red = sqrt(gx_red * gx_red + gy_red * gy_red);

            if(sobel_red > 255)
            {
                sobel_red = 255;
            }
            if(sobel_red < 0)
            {
                sobel_red = 0;
            }

            int gx_green = (pixel_1.rgbtGreen * -1) + (pixel_3.rgbtGreen * 1) + (pixel_4.rgbtGreen * -2) + (pixel_5.rgbtGreen * 2) + (pixel_6.rgbtGreen * -1) + (pixel_8.rgbtGreen * 1);
            int gy_green = (pixel_1.rgbtGreen * -1) + (pixel_2.rgbtGreen * -2) + (pixel_3.rgbtGreen * -1) + (pixel_6.rgbtGreen * 1) + (pixel_7.rgbtGreen * 2) + (pixel_8.rgbtGreen * 1);
            gx_green = abs(gx_green);
            gy_green = abs(gy_green);
            int sobel_green = sqrt(gx_green * gx_green + gy_green * gy_green);

            if(sobel_green > 255)
            {
                sobel_green = 255;
            }
            if(sobel_green < 0)
            {
                sobel_green = 0;
            }

            int gx_blue = (pixel_1.rgbtBlue * -1) + (pixel_3.rgbtBlue * 1) + (pixel_4.rgbtBlue * -2) + (pixel_5.rgbtBlue * 2) + (pixel_6.rgbtBlue * -1) + (pixel_8.rgbtBlue * 1);
            int gy_blue = (pixel_1.rgbtBlue * -1) + (pixel_2.rgbtBlue * -2) + (pixel_3.rgbtBlue * -1) + (pixel_6.rgbtBlue * 1) + (pixel_7.rgbtBlue * 2) + (pixel_8.rgbtBlue * 1);
            gx_blue = abs(gx_blue);
            gy_blue = abs(gy_blue);
            int sobel_blue = sqrt(gx_blue * gx_blue + gy_blue * gy_blue);

            if(sobel_blue > 255)
            {
                sobel_blue = 255;
            }
            if(sobel_blue < 0)
            {
                sobel_blue = 0;
            }

            temp[i][j].rgbtBlue = sobel_blue;
            temp[i][j].rgbtRed = sobel_red;
            temp[i][j].rgbtGreen = sobel_green;
        }
    }

    for(int q = 0; q < height; q++)
    {
        for(int e = 0; e < width; e++)
        {
            image[q][e] = temp[q][e];
        }
    }
    return;
}
