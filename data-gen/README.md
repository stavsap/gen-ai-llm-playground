# Data Generator

wrapping: https://github.com/outlines-dev/outlines


https://www.datacamp.com/tutorial/mistral-7b-tutorial

```shell
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/123
pip install -r requirements.txt
```

### Llama Cpp

https://github.com/abetlen/llama-cpp-python

#### Windows

if there is an issue with llama-cpp-python install:

```text
CMake Error at C:/Users/mriedl/AppData/Local/Temp/pip-build-env-vz70r577/normal/Lib/site-packages/cmake/data/share/cmake-3.27/Modules/CMakeDetermineCompilerId.cmake:503 (message):
        No CUDA toolset found.
```

copy 

```text
CUDA 12.1.props
CUDA 12.1.targets
CUDA 12.1.xml
Nvda.Build.CudaTasks.v12.1.dll

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1\extras\visual_studio_integration\MSBuildExtensions
```

to  

```text
C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\MSBuild\Microsoft\VC\v170\BuildCustomizations
```

by: https://michaelriedl.com/2023/09/10/llama2-install-gpu.html

```shell
set CMAKE_ARGS=-DLLAMA_CUDA=on
set FORCE_CMAKE=1
pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

### Exllamav2 work with GPTQ repos

```shell
git clone https://huggingface.co/TheBloke/CapybaraHermes-2.5-Mistral-7B-GPTQ models/CapybaraHermes-2.5-Mistral-7B-GPTQ
```

### Ninja issue in windows (Exllamav2)

```shell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.\bootstrap-vcpkg.bat
.\vcpkg install openblas:x64-windows
```