# HOW TO SET UP PYTHON ENVIRONMENT FOR VSCODE
## FOR WINDOWS

1. To create virtual environment at the current location:

    ```python -m venv .venv```

2. Select new interpreter python in the .venv/script folder
![Screenshot 2021-08-02 223334](https://user-images.githubusercontent.com/12553570/127953469-c48fa02e-6daf-47d9-86a8-5ff7fd32eb8f.png)

3. Open a new powershell to active (.venv)
![Screenshot 2021-08-02 223550](https://user-images.githubusercontent.com/12553570/127954067-3eb5808a-74c8-4e74-b347-4695f3984acc.png)

4. Install packages:

    ``` pip install scipy```

## FOR MAC
Use conda since pip scipy is not working (yet) with Mac M1.

*Note:* By default, conda creates virtual envs at a central location unlike venv. 
Since I prefer the current location installation I will specific the path.

1. To create virtual environment at the current location

    ```conda create --prefix ./envs```

    *Optional:* step 1 and 4 together:

    ```conda create --prefix ./envs scipy```

2. Restart the Terminal to take effect

    ```conda init zsh```

3. To activate virtual environment

    ```conda activate ./envs```

4. Install packages:

    ```conda install scipy```