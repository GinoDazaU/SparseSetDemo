#include <SFML/Graphics.hpp>
#include "SparseSet.cpp"
#include <cmath>
#include <iostream>

using namespace std;
using namespace sf;

class SparseSetDemo {
private:
    SparseSet sparseSet;
    RenderWindow window;
    vector<RectangleShape> elements;
    vector<Text> texts;
    Font font;
    const int minElementSize = 10;

public:
    SparseSetDemo(int range) : sparseSet(range) {}

    void init(int width, int height, const string &title) {
        window.create(VideoMode(width, height), title);

        if (!font.loadFromFile("../font/arial.ttf")) {
            cout << "Error al cargar la fuente." << endl;
        }

        int paddingX = width * 0.05;
        int paddingY = height * 0.05;

        int effectiveWidth = width - 2 * paddingX;
        int effectiveHeight = height - 2 * paddingY;

        int totalElements = sparseSet.getRange();
        int cols = ceil(sqrt(totalElements));
        int rows = (totalElements + cols - 1) / cols;

        int maxCols = effectiveWidth / (minElementSize);
        int maxRows = effectiveHeight / (minElementSize);
        if (cols > maxCols) {
            cols = maxCols;
            rows = (totalElements + cols - 1) / cols;
        }
        if (rows > maxRows) {
            rows = maxRows;
            cols = (totalElements + rows - 1) / rows;
        }

        int elementSize = min((effectiveWidth - (cols - 1)) / cols, (effectiveHeight - (rows - 1)) / rows);
        elementSize = max(elementSize, minElementSize);

        int gridWidth = cols * elementSize;
        int gridHeight = rows * elementSize;

        int startX = (width - gridWidth) / 2 + paddingX / 2;
        int startY = (height - gridHeight) / 2 + paddingY / 2;

        for (int i = 0; i < totalElements; i++) {
            RectangleShape element(Vector2f(elementSize, elementSize));
            element.setFillColor(Color::White);
            element.setOutlineColor(Color::Black);
            element.setOutlineThickness(1);

            int col = i % cols;
            int row = i / cols;
            element.setPosition(startX + col * elementSize, startY + row * elementSize);

            elements.push_back(element);

            Text text;
            text.setFont(font);
            text.setString(to_string(i));
            text.setCharacterSize(elementSize / 3);
            text.setFillColor(Color::Black);

            FloatRect textBounds = text.getLocalBounds();
            text.setOrigin(textBounds.width / 2, textBounds.height / 2);
            text.setPosition(element.getPosition().x + elementSize / 2, element.getPosition().y + elementSize / 2);

            texts.push_back(text);
        }
    }

    void draw() {
        for (int i = 0; i < elements.size(); i++) {
            if (sparseSet.contains(i)) {
                elements[i].setFillColor(Color::Green);
            } else {
                elements[i].setFillColor(Color::White);
            }
            window.draw(elements[i]);
            window.draw(texts[i]);
        }
    }

    void run() {
        while (window.isOpen()) {
            Event event;
            while (window.pollEvent(event)) {
                if (event.type == Event::Closed) {
                    window.close();
                }

                if (event.type == Event::MouseButtonPressed && event.mouseButton.button == Mouse::Left) {
                    Vector2i mousePos = Mouse::getPosition(window);
                    for (int i = 0; i < elements.size(); i++) {
                        if (elements[i].getGlobalBounds().contains(mousePos.x, mousePos.y)) {
                            if (sparseSet.contains(i)) {
                                sparseSet.erase(i);
                            } else {
                                sparseSet.insert(i);
                            }
                            break;
                        }
                    }
                }
            }

            window.clear(Color(60, 60, 60));
            draw();
            window.display();
        }
    }
};

int main() {
    SparseSetDemo demo(150); // Sparse Set con un rango de 150 elementos
    demo.init(1024, 768, "Sparse Set Demo");
    demo.run();

    return 0;
}
