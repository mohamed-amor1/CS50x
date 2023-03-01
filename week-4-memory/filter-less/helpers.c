#include "helpers.h"
#include <math.h>

int SepiaRed(int r, int g, int b);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0;
            image[i][j].rgbtRed = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtBlue = round(average);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // double sepiaRed = (.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) + (.189 * image[i][j].rgbtBlue);
            // if (sepiaRed > 255)
            //  {
            //     sepiaRed = 255;
            //  }
            double sepiaGreen = (.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) + (.168 * image[i][j].rgbtBlue);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            double sepiaBlue = (.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) + (.131 * image[i][j].rgbtBlue);
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = SepiaRed(image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue);
            image[i][j].rgbtGreen = round(sepiaGreen);
            image[i][j].rgbtBlue = round(sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through rows
    for (int i = 0; i < height; i++)
    {
        // Loop through columns
        for (int j = 0; j < width / 2; j++)
        {
            // Reflect pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // create a temporary image to be blurred
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum_blue;
            int sum_green;
            int sum_red;
            float counter;
            sum_blue = sum_green = sum_red = counter = 0;
            // CORNERS
            // corner pixel on bottom right
            if (i >= 0 && j >= 0)
            {
                sum_red += temp[i][j].rgbtRed;
                sum_green += temp[i][j].rgbtGreen;
                sum_blue += temp[i][j].rgbtBlue;
                counter++;
            }
            // corner pixel on bottom left
            if (i >= 0 && j - 1 >= 0)
            {
                sum_red += temp[i][j - 1].rgbtRed;
                sum_green += temp[i][j - 1].rgbtGreen;
                sum_blue += temp[i][j - 1].rgbtBlue;
                counter++;
            }
            // corner pixel on top left
            if (i - 1 >= 0 && j >= 0)
            {
                sum_red += temp[i - 1][j].rgbtRed;
                sum_green += temp[i - 1][j].rgbtGreen;
                sum_blue += temp[i - 1][j].rgbtBlue;
                counter++;
            }
            // corner pixel on top right
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                sum_red += temp[i - 1][j - 1].rgbtRed;
                sum_green += temp[i - 1][j - 1].rgbtGreen;
                sum_blue += temp[i - 1][j - 1].rgbtBlue;
                counter++;
            }
            // FOUR EDGES
            // pixels on bottom edge
            if ((i >= 0 && j + 1 >= 0) && (i >= 0 && j + 1 < width))
            {
                sum_red += temp[i][j + 1].rgbtRed;
                sum_green += temp[i][j + 1].rgbtGreen;
                sum_blue += temp[i][j + 1].rgbtBlue;
                counter++;
            }
            // pixels on top edge
            if ((i - 1 >= 0 && j + 1 >= 0) && (i - 1 >= 0 && j + 1 < width))
            {
                sum_red += temp[i - 1][j + 1].rgbtRed;
                sum_green += temp[i - 1][j + 1].rgbtGreen;
                sum_blue += temp[i - 1][j + 1].rgbtBlue;
                counter++;
            }
            // pixels on left edge
            if ((i + 1 >= 0 && j >= 0) && (i + 1 < height && j >= 0))
            {
                sum_red += temp[i + 1][j].rgbtRed;
                sum_green += temp[i + 1][j].rgbtGreen;
                sum_blue += temp[i + 1][j].rgbtBlue;
                counter++;
            }
            // pixels on right edge
            if ((i + 1 >= 0 && j - 1 >= 0) && (i + 1 < height && j - 1 >= 0))
            {
                sum_red += temp[i + 1][j - 1].rgbtRed;
                sum_green += temp[i + 1][j - 1].rgbtGreen;
                sum_blue += temp[i + 1][j - 1].rgbtBlue;
                counter++;
            }
            // MIDDLE PIXELS
            // middle pixels
            if ((i + 1 >= 0 && j + 1 >= 0) && (i + 1 < height && j + 1 < width))
            {
                sum_red += temp[i + 1][j + 1].rgbtRed;
                sum_green += temp[i + 1][j + 1].rgbtGreen;
                sum_blue += temp[i + 1][j + 1].rgbtBlue;
                counter++;
            }
            // find average colour value
            image[i][j].rgbtRed = round(sum_red / counter);
            image[i][j].rgbtGreen = round(sum_green / counter);
            image[i][j].rgbtBlue = round(sum_blue / counter);
        }
    }
    return;
}

int SepiaRed(int r, int g, int b)
{
    double sepiaRed = (.393 * r) + (.769 * g) + (.189 * b);
    if (sepiaRed > 255)
    {
        sepiaRed = 255;
    }
    return round(sepiaRed);
}
