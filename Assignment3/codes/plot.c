#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void linspace(double start, double end, int num_points, const char *filename) {
    // Calculate the step size
    double step = (end - start) / (num_points - 1);

    // Open file for writing
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    // Generate and write points to file
    for (int i = 0; i < num_points; i++) {
        double value = start + i * step;
        double y_value = 1.05 * (1 - exp(-(value - 1) / 2));
        fprintf(file, "%lf %lf\n", value, y_value);
    }

    // Close file
    fclose(file);
}

int main() {
    double start = 0.0; // Start value
    double end = 10.0;  // End value
    int num_points = 100; // Number of points
    const char *filename = "linspace_y.txt"; // Output file name

    // Generate linspace and write to file
    linspace(start, end, num_points, filename);

    return 0;
}
